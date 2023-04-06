if 'content-length' not in header_names:
    self._set_content_length(body if body is not None else '')