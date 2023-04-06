def gen():
   raise UnicodeDecodeError('ascii', 'bytes', 0, 1, 'ouch')
gen()