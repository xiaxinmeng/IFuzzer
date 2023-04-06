
from collections import Counter
x = Counter({'a': 0, 'b': 1})
x.update(x)  # works: Counter({'a': 0, 'b': 2})
x += x  # expected: Counter({'a': 0, 'b': 3}) actual: Counter({'b': 3})
