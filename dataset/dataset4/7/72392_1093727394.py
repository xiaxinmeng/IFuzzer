lines = ['first', 'second', 'third']
lines.append('')
assert '\n'.join(lines) == 'first\nsecond\nthird\n'