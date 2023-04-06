import timeit

class Logger(object):
    def __init__(self):
        self._levelprop = self.level = 0

    @property
    def levelprop(self):
        return self.level


def main():
    logger = Logger()
    print(timeit.timeit('logger.level', globals=locals()))
    print(timeit.timeit('logger.levelprop', globals=locals()))

if __name__ == '__main__':
    main()