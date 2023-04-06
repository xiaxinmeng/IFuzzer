
import inspect
import io


class MyBufferedReader(io.BufferedReader):
    """buffer reader class."""


inspect.signature(MyBufferedReader)
