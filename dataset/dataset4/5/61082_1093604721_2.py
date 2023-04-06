parse([], nargs='?')                # get the default value: None
parse([], nargs='*')                # default is None, get arg_strings []
parse([], nargs='*', default=None)  # same case
parse([], nargs='*', default=False) # default is not None, get default
parse([], nargs='*', default=0)     # same case