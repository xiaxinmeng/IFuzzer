def _encode_cdata(text, encoding):
    # escape character data
    try:
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        if encoding:
            return text.encode(encoding, "xmlcharrefreplace")
        else:
            return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)