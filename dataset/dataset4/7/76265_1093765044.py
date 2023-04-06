if os.path.isdir(path):
    url = self.path
    if url.startswith('//'):  # E.g. "//www.python.org/%2f.."
        url = "/." + url  # Becomes "/.//www.python.org/%2f.."
    parts = urllib.parse.urlsplit(url)
    ...