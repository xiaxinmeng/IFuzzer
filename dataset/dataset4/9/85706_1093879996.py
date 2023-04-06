parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument('-verbose', type=int, required=True, dest="bla", help="bla")
known_args, rest_of_args = parser.parse_known_args(["-v", "-verbose=2"])