@contextlib.contextmanager
def captured_output(stream_name):
    """Run the 'with' statement body using a StringIO object in place of a
    specific attribute on the sys module.
    Example use (with 'stream_name=stdout')::

       with captured_stdout() as s:
           print("hello")
       assert s.getvalue() == "hello"
    """
    import io
    orig_stdout = getattr(sys, stream_name)
    setattr(sys, stream_name, io.StringIO())
    try:
        yield getattr(sys, stream_name)
    finally:
        setattr(sys, stream_name, orig_stdout)

def captured_stdout():
    return captured_output("stdout")