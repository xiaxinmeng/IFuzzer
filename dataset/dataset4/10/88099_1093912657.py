class Boom:
    def __enter__(self):
        return self
    def __exit__(self, *_):
        raise AssertionError('boom!')


def main() -> int:
    with Boom():
        raise AssertionError('hi')


if __name__ == '__main__':
    exit(main())