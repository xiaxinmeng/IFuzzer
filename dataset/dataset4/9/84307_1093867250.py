import functools
from unittest import mock


def is_valid():
    return True


def mock_is_valid():
    return False


def decorate(f):
    @functools.wraps(f)
    def decorate_wrapper(*args, **kwargs):
        # This happens in a 3rd-party library
        f.patchings = []
        return f(*args, **kwargs)

    return decorate_wrapper


@decorate
@mock.patch('test.is_valid', new=mock_is_valid)
def test_patch():
    raise Exception()