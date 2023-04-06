
parser.add_argument('-i', '--input', nargs='?',
                    type=lambda s: sys.stdin if '-' == s else open(s, 'r'),
                    default=sys.stdin)
parser.add_argument('-o', '--output', nargs='?',
                    type=lambda s: sys.stdout if '-' == s else open(s, 'w', newline=''),
                    default=sys.stdout)
