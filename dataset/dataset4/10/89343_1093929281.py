sm = SequenceMatcher(None, a, b, autojunk=False)
total = 0
for m in sm.get_matching_blocks():
	print(m, repr(a[m.a : m.a + m.size]))
	total += m.size