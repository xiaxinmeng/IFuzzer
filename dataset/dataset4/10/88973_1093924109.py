
comp = url.split('|')
if len(comp) != 2 or comp[0][-1] not in string.ascii_letters:
    error = 'Bad URL: ' + url
    raise OSError(error)
drive = comp[0][-1].upper()
