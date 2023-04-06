
import re
import pytest

_DIGIT_BOUNDARY_RE = re.compile(
    r'(?<=\D)(?=\d)|(?<=\d)(?=\D)'
)

def test():
    _DIGIT_BOUNDARY_RE.split("10.0.0")
