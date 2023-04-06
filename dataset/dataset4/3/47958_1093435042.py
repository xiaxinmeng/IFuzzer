while len(bytes) < n:
    bytes += read(_urandomfd, n - len(bytes))