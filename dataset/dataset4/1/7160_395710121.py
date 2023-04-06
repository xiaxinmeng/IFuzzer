def _is_binary_files_pair(fsrc, fdst):
    return hasattr(fsrc, 'readinto') and \
        isinstance(fsrc, io.BytesIO) or 'b' in getattr(fsrc, 'mode', '') and \
        isinstance(fdst, io.BytesIO) or 'b' in getattr(fdst, 'mode', '')