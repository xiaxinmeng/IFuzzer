from collections import namedtuple
# create a namedtuple whose members are:
# 00B5;MICRO SIGN;Ll;
# 03BC;GREEK SMALL LETTER MU;Ll
# these are both legal identifier names
names = ['\u00b5', '\u03bc']
for name in names:
    assert name.isidentifier()
mu = namedtuple('mu', names)