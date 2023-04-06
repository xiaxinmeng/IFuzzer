from difflib import ndiff


def main():
    x = '\tx\t=\ty\n\t \t \t^'
    y = '\tx\t=\ty\n\t \t \t^\n'
    print('\n'.join(
        line.rstrip('\n') for line in
        ndiff(x.splitlines(True), y.splitlines(True)))
    )


if __name__ == '__main__':
    exit(main())