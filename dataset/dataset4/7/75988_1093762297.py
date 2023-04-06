import sys
from unittest import mock

def wrapped_func(value):
    raise ValueError(value)