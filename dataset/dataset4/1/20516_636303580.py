
@contextmanager
def safe_space(is_on=True):
    token = IS_SAFE_SPACE_VALUE.set(is_on)
    try:
        yield
    finally:
        IS_SAFE_SPACE_VALUE.reset(token)
