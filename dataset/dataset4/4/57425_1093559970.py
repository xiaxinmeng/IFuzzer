if not hasattr(codecs, 'code_page_encode'):
    raise LookupError("cp65001 encoding is only available on Windows")