

class FinallyIterator:

    def __iter__(self):
        for i in range(10):
            try:
                yield i
            finally:
                print('FINALLY')
