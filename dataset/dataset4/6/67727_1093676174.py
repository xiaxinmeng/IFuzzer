_METHODS_EXPECTING_BODIES = {'OPTIONS', 'POST', 'PUT', 'PATCH'}
if method.upper() in _METHODS_EXPECTING_BODIES and \
        'content-length' not in header_names:
    self._set_content_length(body)