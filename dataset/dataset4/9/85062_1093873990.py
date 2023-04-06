with gzip.open("foo.gz") as gz:
    res = subprocess.run("cat", stdin=gz, capture_output=True)