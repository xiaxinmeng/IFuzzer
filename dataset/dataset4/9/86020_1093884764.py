group = parser.add_mutually_exclusive_group()
group.add_argument('--install-only', action='store_true',
                    help='just install the program, do not run it')
group.add_argument('args', metavar='ARGUMENT', nargs='*', default=None,
                    help='arguments to PROGRAM')