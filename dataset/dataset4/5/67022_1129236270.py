from email.header import Header, make_header, decode

def decode_header_to_string(header):
    """Decode a message header into a string."""

    if not isinstance(header, Header):
        header = make_header(decode_header(header))
    return str(header)