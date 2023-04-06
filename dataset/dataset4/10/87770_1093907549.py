with tempfile.TemporaryDirectory() as dir:
    fifo_path = os.path.join(dir, "fifo")
    os.mkfifo(fifo_path, 0o600)
    ...