expecting_len = method.upper() in _METHODS_EXPECTING_BODIES or \
    body is not None

if expecting_len and 'content-length' not in header_names:
    self._set_content_length(body)