def split(p):
    i = p.rfind('/') + 1
    head, tail = p[:i], p[i:]
    head = head.rstrip('/')
    if not head:
        head = '/'
    return head, tail