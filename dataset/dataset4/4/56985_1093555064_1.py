parser = argparse.ArgumentParser()
parser.add_argument('--foo', type=type_foo_func)
parser.parse_args('--foo bar'.split())