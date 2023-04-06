@pytest.fixture(autouse=True)
def restore_settrace():
    """(Re)store sys.gettrace after test run.

    This is required to re-enable coverage tracking.
    """
    assert sys.gettrace() is _orig_trace

    yield

    newtrace = sys.gettrace()
    if newtrace is not _orig_trace:
        sys.settrace(_orig_trace)
        assert newtrace is None