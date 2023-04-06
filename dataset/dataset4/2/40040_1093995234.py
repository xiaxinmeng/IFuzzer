def open_tar(filename, stream=False):
    mode = "r" + [":", "|"][stream] + "*"
    [...]