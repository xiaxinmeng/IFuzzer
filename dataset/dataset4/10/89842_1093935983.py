
from functools import lru_cache

@lru_cache(typed=True)
def test(arg):
    return str(arg)

print(test((1, 'a')))  # (1, 'a')
print(test((True, 'a')))  # (1, 'a')
