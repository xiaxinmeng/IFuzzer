
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--foo", nargs="+", default=[-1], choices=range(10))
    parser.add_argument("--bar", nargs="*", default=-1, choices=range(10))
    parser.add_argument("pos", nargs="?", default=-1, choices=range(10))
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
