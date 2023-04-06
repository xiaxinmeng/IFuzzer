import os
try: os.rmdir('nonexist')
except Exception as e:
    print(repr(e.args[1]), '\n', repr(e.strerror), '\n', e.filename)
os.rmdir('nonexist')