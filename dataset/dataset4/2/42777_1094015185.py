import locale
locale.setlocale(locale.LC_NUMERIC, 'de_DE')
u'%.1f' % 1.0
assert '1.0' == u'%.1f' % 1.0