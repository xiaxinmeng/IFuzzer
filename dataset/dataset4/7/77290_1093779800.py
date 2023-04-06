parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)
subparsers.add_parser('foo')
parser.parse_args()