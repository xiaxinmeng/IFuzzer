async def helper(value):
    return value


async def test_foo():
    with patch("bar", return_value=helper(42)):
        assert await foo() == 42