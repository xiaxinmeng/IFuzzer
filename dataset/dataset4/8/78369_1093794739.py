import argparse

parser = argparse.ArgumentParser(prog='game.py')
parser.add_argument('move', choices={'rock':'a', 'paper':'b', 'scissors':'c'})
print(parser.parse_args(['rock']))