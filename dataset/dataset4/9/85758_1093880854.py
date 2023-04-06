def add_subparser(name: str, subparser: _SubParsersAction, subparsers: dict) -> ArgumentParser:
    parser = subparser.add_parser(name)
    parser.add_argument('-v', '--verbose', action='store_true')
    subparsers[name] = parser
    return parser