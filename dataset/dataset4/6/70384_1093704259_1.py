# {{{
import optparse

def try_args(*args):
    parser = optparse.OptionParser()
    parser.add_option("-a")
    print("Trying:", args)
    try:
        print(parser.parse_args(list(args)))
    except SystemExit:
        print("FAILED!")

try_args("-a", "-")  # Works
try_args("-a", "-a")  # Works
try_args("-a", "--")  # Works
try_args("-a", "--things--")  # Works
# }}}