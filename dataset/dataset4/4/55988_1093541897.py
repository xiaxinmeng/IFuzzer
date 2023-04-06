def support_sparse_file(directory):
    import tempfile

    with tempfile.NamedTemporaryFile(dir=directory) as tmpfile:
        # Create a file with a size of 1 byte but without content
        # (only zeros)
        with open(tmpfile.name, "wb") as f:
            f.truncate(1)
        filestat = os.stat(tmpfile.name)
        return (filestat.st_blocks == 0)