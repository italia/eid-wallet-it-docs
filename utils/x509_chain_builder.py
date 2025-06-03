from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import ExtensionOID

from cryptography.hazmat.primitives.asymmetric import rsa, ec

import binascii
import textwrap

def format_name(name):
    return ", ".join(f"{attr.oid._name}={attr.value}" for attr in name)

def format_serial(serial):
    return f"{serial} (0x{serial:x})"

def format_time(dt):
    return dt.strftime("%b %d %H:%M:%S %Y GMT")

def format_name_constraints(nc):
    lines = []
    if nc.permitted_subtrees:
        lines.append("                Permitted:")
        for idx, subtree in enumerate(nc.permitted_subtrees, 1):
            if isinstance(subtree, x509.DNSName):
                lines.append(f"                  DNS.{idx}={subtree.value}")
            elif isinstance(subtree, x509.UniformResourceIdentifier):
                lines.append(f"                  URI.{idx}={subtree.value}")
            elif isinstance(subtree, x509.IPAddress):
                lines.append(f"                  IP.{idx}={subtree.value}")
            elif isinstance(subtree, x509.DirectoryName):
                lines.append(f"                  DirName.{idx}={format_name(subtree.value)}")
            else:
                lines.append(f"                  {type(subtree).__name__}.{idx}={subtree.value}")
    if nc.excluded_subtrees:
        lines.append("                Excluded:")
        for idx, subtree in enumerate(nc.excluded_subtrees, 1):
            if isinstance(subtree, x509.DNSName):
                lines.append(f"                  DNS.{idx}={subtree.value}")
            elif isinstance(subtree, x509.UniformResourceIdentifier):
                lines.append(f"                  URI.{idx}={subtree.value}")
            elif isinstance(subtree, x509.IPAddress):
                lines.append(f"                  IP.{idx}={subtree.value}")
            elif isinstance(subtree, x509.DirectoryName):
                lines.append(f"                  DirName.{idx}={format_name(subtree.value)}")
            else:
                lines.append(f"                  {type(subtree).__name__}.{idx}={subtree.value}")
    return "\n".join(lines) if lines else "                (none)"

def format_pubkey(pubkey):
    if isinstance(pubkey, rsa.RSAPublicKey):
        key_type = "RSA"
        key_size = pubkey.key_size
        numbers = pubkey.public_numbers()
        modulus = numbers.n
        exponent = numbers.e
        mod_bytes = modulus.to_bytes((modulus.bit_length() + 7) // 8, "big")
        mod_hex = binascii.hexlify(mod_bytes).decode()
        mod_lines = textwrap.wrap(mod_hex, 32)
        mod_lines = [
            "                    " + ":".join(a+b for a, b in zip(line[::2], line[1::2]))
            for line in mod_lines
        ]
        return (
            f"            Public Key Algorithm: rsaEncryption ({key_type})\n"
            f"                Public-Key: ({key_size} bit)\n"
            f"                Modulus:\n" +
            "\n".join(mod_lines) + "\n"
            f"                Exponent: {exponent} (0x{exponent:x})"
        )
    elif isinstance(pubkey, ec.EllipticCurvePublicKey):
        key_type = "EC"
        key_size = pubkey.key_size
        numbers = pubkey.public_numbers()
        curve = pubkey.curve.name
        x = numbers.x
        y = numbers.y
        return (
            f"            Public Key Algorithm: id-ecPublicKey ({key_type})\n"
            f"                Public-Key: ({key_size} bit)\n"
            f"                Curve: {curve}\n"
            f"                X: {x}\n"
            f"                Y: {y}"
        )
    else:
        key_type = type(pubkey).__name__
        return f"            Public Key Algorithm: (unknown: {key_type})"

def format_basic_constraints(bc):
    s = f"                CA:{'TRUE' if bc.ca else 'FALSE'}"
    if bc.path_length is not None:
        s += f", pathlen:{bc.path_length}"
    return s

def format_key_usage(ku):
    usages = []
    if ku.digital_signature: usages.append("Digital Signature")
    if ku.content_commitment: usages.append("Content Commitment")
    if ku.key_encipherment: usages.append("Key Encipherment")
    if ku.data_encipherment: usages.append("Data Encipherment")
    if ku.key_agreement: usages.append("Key Agreement")
    if ku.key_cert_sign: usages.append("Certificate Sign")
    if ku.crl_sign: usages.append("CRL Sign")
    if ku.key_agreement:
        try:
            if ku.encipher_only: usages.append("Encipher Only")
        except ValueError:
            pass
        try:
            if ku.decipher_only: usages.append("Decipher Only")
        except ValueError:
            pass
    return "                " + ", ".join(usages)

def format_ext_key_usage(eku):
    return "                " + ", ".join(oid._name or oid.dotted_string for oid in eku)

def format_subject_alt_name(san):
    lines = []
    for name in san:
        if isinstance(name, x509.DNSName):
            lines.append(f"                DNS:{name.value}")
        elif isinstance(name, x509.IPAddress):
            lines.append(f"                IP:{name.value}")
        elif isinstance(name, x509.RFC822Name):
            lines.append(f"                Email:{name.value}")
        elif isinstance(name, x509.UniformResourceIdentifier):
            lines.append(f"                URI:{name.value}")
        else:
            lines.append(f"                {type(name).__name__}:{name.value}")
    return "\n".join(lines)

def format_subject_key_id(ski):
    return "                " + ":".join(textwrap.wrap(binascii.hexlify(ski.digest).decode(), 2))

def format_authority_key_id(aki):
    if aki.key_identifier:
        return "                keyid:" + ":".join(textwrap.wrap(binascii.hexlify(aki.key_identifier).decode(), 2))
    return ""

def format_crl_distribution_points(crl):
    lines = []
    for dp in crl:
        lines.append("                Full Name:")
        if dp.full_name:
            for name in dp.full_name:
                if isinstance(name, x509.UniformResourceIdentifier):
                    lines.append(f"                  URI:{name.value}")
                elif isinstance(name, x509.DirectoryName):
                    lines.append(f"                  DirName:{format_name(name.value)}")
                else:
                    lines.append(f"                  {type(name).__name__}:{name.value}")
        else:
            lines.append("                  (no full name)")
    return "\n".join(lines) if lines else "                (none)"

def format_signature(sig_bytes):
    hexstr = binascii.hexlify(sig_bytes).decode()
    lines = textwrap.wrap(hexstr, 32)
    return "\n".join("     " + ":".join(a+b for a, b in zip(line[::2], line[1::2])) for line in lines)

def format_certificate(cert):
    lines = []
    lines.append("Certificate:")
    lines.append("    Data:")
    lines.append(f"        Version: {cert.version.value + 1} (0x{cert.version.value:x})")
    lines.append(f"        Serial Number: {format_serial(cert.serial_number)}")
    lines.append(f"    Signature Algorithm: {cert.signature_hash_algorithm.name if cert.signature_hash_algorithm else 'unknown'}")
    lines.append(f"        Issuer: {format_name(cert.issuer)}")
    lines.append(f"        Validity")
    lines.append(f"            Not Before: {format_time(cert.not_valid_before)}")
    lines.append(f"            Not After : {format_time(cert.not_valid_after)}")
    lines.append(f"        Subject: {format_name(cert.subject)}")
    lines.append(f"        Subject Public Key Info:")
    lines.append(format_pubkey(cert.public_key()))
    lines.append(f"        X509v3 extensions:")
    for ext in cert.extensions:
        if ext.oid == ExtensionOID.BASIC_CONSTRAINTS:
            lines.append("            X509v3 Basic Constraints:")
            lines.append(format_basic_constraints(ext.value))
        elif ext.oid == ExtensionOID.KEY_USAGE:
            lines.append("            X509v3 Key Usage:")
            lines.append(format_key_usage(ext.value))
        elif ext.oid == ExtensionOID.EXTENDED_KEY_USAGE:
            lines.append("            X509v3 Extended Key Usage:")
            lines.append(format_ext_key_usage(ext.value))
        elif ext.oid == ExtensionOID.SUBJECT_ALTERNATIVE_NAME:
            lines.append("            X509v3 Subject Alternative Name:")
            lines.append(format_subject_alt_name(ext.value))
        elif ext.oid == ExtensionOID.SUBJECT_KEY_IDENTIFIER:
            lines.append("            X509v3 Subject Key Identifier:")
            lines.append(format_subject_key_id(ext.value))
        elif ext.oid == ExtensionOID.AUTHORITY_KEY_IDENTIFIER:
            lines.append("            X509v3 Authority Key Identifier:")
            lines.append(format_authority_key_id(ext.value))
        elif ext.oid == ExtensionOID.CRL_DISTRIBUTION_POINTS:
            lines.append("            X509v3 CRL Distribution Points:")
            lines.append(format_crl_distribution_points(ext.value))
        elif ext.oid == ExtensionOID.NAME_CONSTRAINTS:
            lines.append("            X509v3 Name Constraints:")
            lines.append(format_name_constraints(ext.value))
        else:
            lines.append(f"            {ext.oid._name or ext.oid.dotted_string}:")
            lines.append(f"                {ext.value}")
    lines.append("")
    lines.append(f"    Signature Algorithm: {cert.signature_hash_algorithm.name if cert.signature_hash_algorithm else 'unknown'}")
    lines.append(format_signature(cert.signature))
    lines.append("")
    return "\n".join(lines)

# Example usage:
der_certs = gen_chain() # from pyeudiw.tests.x509.test_x509 import gen_chain

for der in der_certs:
    cert = x509.load_der_x509_certificate(der)
    print(format_certificate(cert))
    # Print PEM
    pem = cert.public_bytes(serialization.Encoding.PEM)
    print(pem.decode())
