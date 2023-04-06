
import multiprocessing

def main():
    q = multiprocessing.Queue()
    q.put(0)

if __name__ == '__main__':
    main()
