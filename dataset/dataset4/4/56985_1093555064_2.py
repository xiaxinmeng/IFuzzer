parser = argparse.ArgumentParser()
parser.add_argument('--foo', type=type_foo_func, default='foo')
parser.parse_args('')