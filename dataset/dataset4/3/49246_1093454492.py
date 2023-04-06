import io, os
fd = os.open("/etc/issue", os.O_RDONLY)
raw = open(fd, "rb", buffering=0)
text = io.TextIOWrapper(raw, line_buffering=False)
print(text.read(1))