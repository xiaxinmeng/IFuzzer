def get_tokens(source):
    if hasattr(source, "encode"):
        # Already decoded, so bypass encoding detection
        return _tokenize(io.StringIO(source).readline, None)
    # Otherwise attempt to detect the correct encoding
    return tokenize(io.BytesIO(source).readline)