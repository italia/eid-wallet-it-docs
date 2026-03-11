"""
svg2pdf.py - Utility to convert SVG images to PDF format.
"""

import sys
#import argparse
from pathlib import Path
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

#----------------------------------
# Convert an SVG file to PDF format
#----------------------------------
def convert_svg_to_pdf(input_file: str, output_dir: str = None) -> str:
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"Error: File not found: {input_file}")
        return None

    # If input is not an SVG file, skip it
    if input_path.suffix.lower() != '.svg':
        print(f"Skipping non-SVG file: {input_file}")
        return None

    # Determine output path (same name, but in output_dir if specified)
    if output_dir:
        output_path = Path(output_dir) / input_path.with_suffix('.pdf').name
    else:
        output_path = input_path.with_suffix('.pdf')

    try:
        # Create output directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # SVG → PDF conversion
        drawing = svg2rlg(str(input_path))
        renderPDF.drawToFile(drawing, str(output_path))

        print(f"Conversion completed: {input_path} → {output_path}")
        return str(output_path)
    except Exception as e:
        print(f"Error during conversion: {e}")
        return None

#--------------------------------------------------
#Convert all SVG files in a directory to PDF format
#--------------------------------------------------
def convert_directory(input_dir: str, output_dir: str = None) -> int:
    input_path = Path(input_dir)
    if not input_path.is_dir():
        print(f"Error: Directory not found: {input_dir}")
        return 0

    # Find all SVG files in the directory
    svg_files = list(input_path.glob("*.svg"))

    if not svg_files:
        print(f"No SVG files found in {input_dir}")
        return 0

    successful = 0
    for svg_file in svg_files:
        if convert_svg_to_pdf(str(svg_file), output_dir):
            successful += 1

    return successful

#-----------------
#Prompt usage info
#-----------------
def show_usage():
    """Display usage information."""
    print("Usage: svg2pdf.py [options] <svg_file(s)>")
    print("       svg2pdf.py -d <input_directory> [options]")
    print("\nOptions:")
    print("  -h, --help                  Show this help message and exit")
    print("  -d, --dir <directory>       Process input as directory (convert all SVG files in it)")
    print("  -o, --output <directory>    Specify output directory for PDF files")
    print("\nExamples:")
    print("  svg2pdf.py image.svg                    # Convert single SVG file")
    print("  svg2pdf.py image1.svg image2.svg        # Convert multiple SVG files")
    print("  svg2pdf.py -d svgs/                     # Convert all SVGs in directory")
    print("  svg2pdf.py image.svg -o pdfs/           # Convert file and save to specific directory")
    print("  svg2pdf.py -d svgs/ -o pdfs/            # Convert all SVGs in svgs/ and save to pdfs/")

#-----------
# Main func
#-----------
def main():

    args = sys.argv[1:]

    if not args:
        show_usage()
        return

    if '-h' in args or '--help' in args:
        show_usage()
        return

    input_dir = None
    output_dir = None
    input_files = []
    dir_mode = False

    # Process args
    i = 0
    while i < len(args):
        if args[i] == '-d' or args[i] == '--dir':
            dir_mode = True
            if i + 1 < len(args) and not args[i+1].startswith('-'):
                input_dir = args[i+1]
                i += 2
            else:
                print("Error: No directory specified after -d/--dir flag")
                show_usage()
                return
        elif args[i] == '-o' or args[i] == '--output':
            if i + 1 < len(args) and not args[i+1].startswith('-'):
                output_dir = args[i+1]
                i += 2
            else:
                print("Error: No directory specified after -o/--output flag")
                show_usage()
                return
        elif args[i].startswith('-'):
            print(f"Error: Unknown option {args[i]}")
            show_usage()
            return
        else:
            input_files.append(args[i])
            i += 1

    # Execute in directory mode
    if dir_mode:
        if not input_dir:
            print("Error: No input directory specified")
            show_usage()
            return

        if input_files:
            print("Warning: Additional arguments ignored in directory mode")

        num_converted = convert_directory(input_dir, output_dir)
        print(f"Successfully converted {num_converted} SVG files")
        return

    # Otherwise, process individual files
    if not input_files:
        print("Error: No input files specified")
        show_usage()
        return

    successful = 0
    for input_file in input_files:
        if convert_svg_to_pdf(input_file, output_dir):
            successful += 1

    print(f"Successfully converted {successful} out of {len(input_files)} files")


if __name__ == "__main__":
    main()


