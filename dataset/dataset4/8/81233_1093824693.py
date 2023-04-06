from unittest.mock import AsyncMock, patch
import asyncio

async def foo():
    pass

async def post(url):
    pass


class Response:

    async def json(self):
        pass

    def sync_json(self):
        return foo() # Returns a coroutine which should be awaited to get the result


async def main():
    # post function is an async function and hence AsyncMock is returned.
    with patch(f"{__name__}.post", return_value={'a': 1}) as m:
        print(await post("http://example.com"))

    # The json method call is a coroutine whose return_value is set with the dictionary
    # json is an async function and hence during patching here m is an AsyncMock
    response = Response()
    with patch.object(response, 'json', return_value={'a': 1}):
        print(await response.json())

    # sync_json returns a coroutine and not an async def itself. So it's mocked as MagicMock
    # by patch.object and we need to pass an explicit callable as AsyncMock to make sure it's
    # awaitable
    response = Response()
    with patch.object(response, 'sync_json', AsyncMock(return_value={'a': 1})):
        print(await response.sync_json())


asyncio.run(main())