class Some:
    x: int = None

import typing
assert typing.get_type_hints(Some) == {'x': int}