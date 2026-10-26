#!/usr/bin/env python3
"""Compare the remote-flow QR figures with the plaintext payload included by the spec.

The expected payload is the file included from both editions of remote-flow.rst.
The URL is not hardcoded: when that text changes, this check fails until the
figures encode the new text.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
PAYLOAD_NAME = "remote-flow-qr.txt"
EDITIONS = (
    ROOT / "docs/en/remote-flow.rst",
    ROOT / "docs/it/remote-flow.rst",
)
FIGURES = (
    ROOT / "docs/en/images/svg/verifier_qr_code.svg",
    ROOT / "docs/it/images/svg/verifier_qr_code.svg",
    ROOT / "docs/en/images/pdf/verifier_qr_code.pdf",
    ROOT / "docs/it/images/pdf/verifier_qr_code.pdf",
)
INCLUDE_RE = re.compile(r"^\s*\.\.\s+literalinclude::\s+(\S+)\s*$", re.MULTILINE)


class CheckError(Exception):
    """The included text and a QR figure do not agree."""


def payload_include(rst_path: Path) -> Path:
    text = rst_path.read_text(encoding="utf-8")
    found = []
    for match in INCLUDE_RE.finditer(text):
        resolved = (rst_path.parent / match.group(1)).resolve()
        if resolved.name == PAYLOAD_NAME:
            found.append(resolved)
    if len(found) != 1:
        raise CheckError(
            f"{rst_path.relative_to(ROOT)} must include {PAYLOAD_NAME} once, found {len(found)}"
        )
    if not found[0].is_file():
        raise CheckError(f"missing payload file {found[0]}")
    return found[0]


def expected_payload() -> tuple[Path, bytes]:
    includes = [payload_include(path) for path in EDITIONS]
    if includes[0] != includes[1]:
        raise CheckError(
            "the two editions include different QR payload files: "
            f"{includes[0]} and {includes[1]}"
        )
    payload = includes[0].read_text(encoding="utf-8").strip().encode("utf-8")
    if not payload:
        raise CheckError(f"{includes[0]} is empty")
    return includes[0], payload


def decode_image(image: Image.Image) -> bytes:
    from pyzbar.pyzbar import decode

    gray = ImageOps.grayscale(image)
    candidates = (
        image.convert("RGB"),
        gray,
        gray.point(lambda pixel: 0 if pixel < 128 else 255),
    )
    for candidate in candidates:
        symbols = decode(candidate)
        if not symbols:
            continue
        payloads = [symbol.data for symbol in symbols]
        if len(payloads) != 1:
            raise CheckError(f"expected one QR symbol, found {len(payloads)}")
        return payloads[0]
    raise CheckError("no QR symbol found")


def render_svg(path: Path) -> Image.Image:
    from reportlab.graphics import renderPM
    from svglib.svglib import svg2rlg

    drawing = svg2rlg(str(path))
    if drawing is None:
        raise CheckError(f"cannot render {path.relative_to(ROOT)}")
    return renderPM.drawToPIL(drawing, dpi=144)


def render_pdf(path: Path) -> Image.Image:
    with tempfile.TemporaryDirectory() as tmp:
        prefix = str(Path(tmp) / "qr")
        subprocess.run(
            ["pdftoppm", "-png", "-r", "200", "-singlefile", str(path), prefix],
            check=True,
            capture_output=True,
        )
        with Image.open(prefix + ".png") as rendered:
            rendered.load()
            return rendered.copy()


def decode_figure(path: Path) -> bytes:
    if not path.is_file():
        raise CheckError(f"missing figure {path.relative_to(ROOT)}")
    if path.suffix.lower() == ".svg":
        image = render_svg(path)
    elif path.suffix.lower() == ".pdf":
        image = render_pdf(path)
    else:
        raise CheckError(f"unsupported figure {path.relative_to(ROOT)}")
    return decode_image(image)


def main() -> int:
    try:
        source, expected = expected_payload()
        for figure in FIGURES:
            actual = decode_figure(figure)
            if actual != expected:
                raise CheckError(
                    f"{figure.relative_to(ROOT)} does not match {source.relative_to(ROOT)}\n"
                    f"figure: {actual.decode('utf-8', errors='replace')}\n"
                    f"text:   {expected.decode('utf-8')}"
                )
    except CheckError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or b"").decode("utf-8", errors="replace").strip()
        print(f"error: pdftoppm failed: {detail}", file=sys.stderr)
        return 1
    print(f"remote-flow QR figures match {source.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
