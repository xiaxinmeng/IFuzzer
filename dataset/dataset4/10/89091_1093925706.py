
def test_async_fn():
    async def async_fn():
        pass

    async_fn()


def test_async_gen_fn():
    async def agen_fn():
        yield

    agen_fn().aclose()
    agen_fn().asend(None)

test_async_fn()
test_async_gen_fn()
