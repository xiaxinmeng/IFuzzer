
x = Counter({'a': 1})
x += Counter({'a': 0})  # ok: Counter({'a': 1})

y = Counter({'a': 0})
y += y  # expected: Counter({'a': 0}) actual: Counter()
