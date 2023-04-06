if url[:2] == '//' and url[2:3] != '/' and url[2:12].lower() != 'localhost/':
    raise ValueError("file:// scheme is supported only on localhost")