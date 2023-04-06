# {{{
import argparse

def try_args(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-a")
    print("Trying:", args)
    try:
        print(parser.parse_args(args))
    except SystemExit:
        print("FAILED!")

try_args("-a", "-")  # Works fine
try_args("-a", "-a")  # Breaks
try_args("-a", "--")  # Breaks
try_args("-a", "--things--")  # Breaks
# }}}