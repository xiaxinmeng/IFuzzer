class CM:

    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise RuntimeError()

if __name__ == '__main__':
    with CM() as cm:
        print('Hello')