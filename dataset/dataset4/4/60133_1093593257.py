import argparse

if __name__ == '__main__':
    argParser = argparse.ArgumentParser()
    argParser.add_argument('--foo+', action='store_true')
    arguments = argParser.parse_args()