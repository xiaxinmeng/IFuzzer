import multiprocessing

def main():
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    print("create.py complete")

if __name__ == '__main__':
    main()