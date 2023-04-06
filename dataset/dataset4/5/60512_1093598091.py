def main(args):
    print('main: %s' % args)
...
parser.set_defaults(func=main)
...
args = parser.parse_args('')
args.func(args)