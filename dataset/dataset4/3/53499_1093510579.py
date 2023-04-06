sub = parser.add_subparsers()
info = sub.add_parser("info")
main = sub.add_parser("main")
sub.default = main