
import inspect
import io

from io import DEFAULT_BUFFER_SIZE


class MyBufferedReader(io.BufferedReader):
    """buffer reader class."""


inspect.signature(MyBufferedReader)
