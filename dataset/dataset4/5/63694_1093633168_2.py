T = TypeVar('T')


@contextmanager
def sample_before_and_after(cb: Callable[[T, T], None], sample: Callable[[], T]):
    before = sample()
    try:
        yield
    finally:
        after = sample()
        cb(before, after)