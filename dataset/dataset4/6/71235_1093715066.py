out = subprocess.check_output(
    ...,
    stderr=subprocess.STDOUT,
    # No universal_newlines!
)
...
out = io.TextIOWrapper(io.BytesIO(out), errors="surrogateescape").read()