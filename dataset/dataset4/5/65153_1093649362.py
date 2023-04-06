import multiprocessing


def main():
    p = multiprocessing.Process(target=lambda: None)
    p.start()
    p.join()


if __name__ == '__main__':
    main()