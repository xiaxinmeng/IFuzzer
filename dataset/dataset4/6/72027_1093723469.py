import functools
hello = functools.partial(print, "Hello World", end='!\n')
hello()