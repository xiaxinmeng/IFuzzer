if netloc or (scheme and scheme in uses_netloc and url[:2] != '//'):
    if url and url[:1] != '/' and scheme in ("file", ""): # my change
        url = '/' + url