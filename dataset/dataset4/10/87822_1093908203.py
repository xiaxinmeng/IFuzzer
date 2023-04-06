import traceback, sys

def format_exception_chunks(exception):
    return (traceback.TracebackException.from_exception(exception, capture_locals=True).format())

def print_exception(_ignored_type, exception, _ignored_traceback):
    for chunk in format_exception_chunks(exception):
        print(chunk, file=sys.stderr, end="")

# This change to sys.excepthook adds local variables to stack traces.
sys.excepthook = print_exception