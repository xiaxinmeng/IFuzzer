
import asyncio


async def hello_world():
    """
    Will greet the world with a friendly hello.

    >>> asyncio.run(hello_world())
    'hello world'

    """
    return "hello world"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
