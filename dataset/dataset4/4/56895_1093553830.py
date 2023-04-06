parser = argparse.ArgumentParser()
sub = parser.add_subparsers()
somecommand_help = sub.add_parser('somecommand-help', hide=True)