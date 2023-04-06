parser = ArgumentParser()
parser.add_argument("--test", dest="test", action='store', type=str, default=False)
args = parser.parse_args()
print(repr(args.test))

to_str = lambda s: s.lower()

parser = ArgumentParser()
parser.add_argument("--test", dest="test", action='store', type=to_str, default=False)
args = parser.parse_args()
print(repr(args.test))