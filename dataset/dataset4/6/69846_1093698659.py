if not text.strip('T'):
    if state == 0:
        return text + 'T'
    else:
        return None