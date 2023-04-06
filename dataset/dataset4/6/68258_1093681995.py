
"""
$ python exception-in-with.py
EXPECTED
Traceback (most recent call last):
  File "exception-in-with.py", line 51, in <module>
    abc  # !!!
NameError: name 'abc' is not defined
ACTUAL
usage: exception-in-with.py [-h] --image_path PATH
exception-in-with.py: error: argument --image_path is required

$ python exception-in-with.py --image_path x
EXPECTED == ACTUAL
Traceback (most recent call last):
  File "exception-in-with.py", line 51, in <module>
    abc  # !!!
NameError: name 'abc' is not defined

$ python exception-in-with.py --image_path x --tile_indices 1
EXPECTED
Traceback (most recent call last):
  File "exception-in-with.py", line 51, in <module>
    abc  # !!!
NameError: name 'abc' is not defined
ACTUAL
usage: exception-in-with.py [-h] --image_path PATH
exception-in-with.py: error: unrecognized arguments: --tile_indices 1
"""
from argparse import ArgumentParser


class Starter(object):

    def __init__(self):
        self.argument_parser = ArgumentParser()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.argument_parser.parse_args()

    def add_argument(self, *args, **kw):
        self.argument_parser.add_argument(*args, **kw)


with Starter() as starter:
    starter.add_argument('--image_path', metavar='PATH', required=True)
    abc  # !!!
    starter.add_argument('--tile_indices', metavar='INTEGER')
