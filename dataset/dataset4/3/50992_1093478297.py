def pprint(object='\n', *args, stream=None, indent=1, width=80, depth=None):
    """Pretty-print a Python object to a stream [default is sys.stdout]."""
    printer = PrettyPrinter(
        stream=stream, indent=indent, width=width, depth=depth)
    printer.pprint(object)
    for arg in args:
        printer.pprint(arg)