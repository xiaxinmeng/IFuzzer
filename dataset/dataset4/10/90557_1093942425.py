from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    # A lie for type checkers to work.
    from something_that_doesnt_exist_at_runtime import dict_keys, dict_values
else:
    # Runtime doesn't check type annotations anyway.
    dict_keys = Any
    dict_values = Any