def validate_url(url):
    parts = urlparse.urlparse(url.strip())
    # scheme, netloc, path, params, query, fragment
    # XXX: preserve backward compatibility w/ old code
    if not parts.scheme:
        parts = parts._replace(scheme='http', netloc=parts.path.strip('/'), path='')

    # remove params, query, and fragment
    # params is nearly never used anywhere
    # (NOTE: it does NOT mean the stuff after '?')
    # it actually means this http://domain/page.py;param1=foo?query1=bar
    # query and fragment are used but aren't helpful for our application
    parts = parts._replace(params='', query='', fragment='')

    if parts.scheme not in URI_SCHEMES:
        raise ValueError('scheme=%s is not valid' % parts.scheme)
    if '.' not in parts.netloc:
        raise ValueError('location=%s does not contain a domain' % parts.netloc)

    if len(parts.path) and not parts.path.startswith('/'):
        raise ValueError('path=%s appears invalid' % parts.path)
    elif not parts.path:
        parts=parts._replace(path='/')

    validated_url = parts.geturl()
    return validated_url, parts