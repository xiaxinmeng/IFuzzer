
from collections.abc import Mapping, Sequence
import sys
if sys.version_info <= (2, 7):
    assert '__reversed__' not in dir(Mapping)
elif sys.version_info >= (3, 7):
    assert not isinstance(Mapping, Sequence)
    assert '__reversed__' in dir(Mapping)
    assert list(reversed(dict.fromkeys('abc'))) == ['c', 'b', 'a']
    # + no mention of Mapping.__reversed__ in the docs
