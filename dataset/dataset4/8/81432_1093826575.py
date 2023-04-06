from collections.abc import Awaitable
from unittest.mock import patch

class NewCoroutine(Awaitable):
    def __await__():
        pass

obj = NewCoroutine()

with patch(f"{__name__}.obj") as m:
    print(m)