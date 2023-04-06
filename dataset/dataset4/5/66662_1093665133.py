if not e.args:
    msg = ''
elif len(e.args) == 1:
    msg = str(e.args[0])
elif len(e.args) <= 5:
    msg = '[Error %s] %s' % e.args[:2]
    if len(e.args) > 2:
        msg = '%s: %r' % (msg, e.args[2]) # filename
    if len(e.args) > 4:
        msg = '%s -> %r' % (msg, e.args[4]) # filename2
else:
    msg = str(e.args)