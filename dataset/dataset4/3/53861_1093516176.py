parser = argparse.ArgumentParser(add_help=False)
flags = parser.add_argument_group('My Optional Arguments')
flags.add_argument('-h', '--help', action='help')
flags.add_argument('-v', action='version', version='1.3')