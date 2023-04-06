parser = argparse.ArgumentParser(greedy_star=True)
add = parser.add_argument
add('--tracks', choices=['40', '80'])
add('image', nargs='*', action=_CustomAction)
parser.parse_args()