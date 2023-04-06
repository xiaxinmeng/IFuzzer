from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    outer = parser.add_mutually_exclusive_group(required=True)
    outer.add_argument('-a')
    inner = outer.add_mutually_exclusive_group()
    inner.add_argument('-b')
    inner.add_argument('-c')
    parser.parse_args()


if __name__ == '__main__':
    main()