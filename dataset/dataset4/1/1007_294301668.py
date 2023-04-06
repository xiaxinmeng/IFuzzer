
assert get_pattern(l('foo/bar')) == l(re.escape('foo/bar') + r'\Z(?ms)')
