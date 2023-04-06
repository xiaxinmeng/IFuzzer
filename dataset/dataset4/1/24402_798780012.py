
# Ignores a single newline at the end, regardless of `=`.
a2b_base64(ascii, ignore_trailing_newline=True)  # Make this the default.
# and
a2b_base64(ascii, ignore_trailing_newline=False)   # No extra data is allowed ever (raises an Error).
