
from typing import assert_type

def parse_int(value) -> int:
    # Hmm. A casual observer would likely read this incorrectly as `assert isinstance(value, str)`...
    assert_type(value, str)
    return int(value)
