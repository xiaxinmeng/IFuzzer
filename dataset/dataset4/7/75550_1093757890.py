
from re import *

def foo(flag: RegexFlag):
    return match("[a-z]+", "ABC", flag)

print(foo(IGNORECASE))
print(foo(VERBOSE))
