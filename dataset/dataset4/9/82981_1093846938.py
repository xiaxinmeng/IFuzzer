import codecs
codecs.register_error('err', lambda err: (b'x', err.end + 1))
assert repr(u'\uDD00yz'.encode('utf8', errors='err')) == b'xz'