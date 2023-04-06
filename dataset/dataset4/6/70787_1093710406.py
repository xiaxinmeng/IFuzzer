
from threading import Thread
from mock.mock import MagicMock


def main():
    mocks = [MagicMock() for _ in range(1000)]

    def in_thread():
        for m in mocks:
            str(m)

    threads = [Thread(target=in_thread) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
