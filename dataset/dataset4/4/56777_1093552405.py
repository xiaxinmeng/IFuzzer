def wcwidth(c, legacy_cjk=False):
	if c in u'\t\r\n\10\13\14': raise ValueError('character %r has no intrinsic width' % c)
	if c in u'\0\5\7\16\17': return 0
	if u'\u1160' <= c <= u'\u11ff': return 0 # hangul jamo
	if unicodedata.category(c) in ('Mn', 'Me', 'Cf') and c != u'\u00ad': return 0 # 00ad = soft hyphen
	eaw = unicodedata.east_asian_width(c)
	if eaw in ('F', 'W'): return 2
	if legacy_cjk and eaw == 'A': return 2
	return 1