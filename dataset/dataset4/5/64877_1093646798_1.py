m = re.match(".+?: (\d+)\n((?:.+\n){\1})", d)
print(m)
# prints: None
# Expected a match object.
print(m.groups())
# Causes Exception.
# Expected: ('3', '1\n2\n3\n')

# Works with hard coded match length.
m = re.match(".+?: (\d+)\n((?:.+\n){3})", d)
print(m.groups())
('3', '1\n2\n3\n')