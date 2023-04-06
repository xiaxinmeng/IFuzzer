
import multiprocessing as mp
import time

def demo(f):
    print(f)

def main():
    cxt=mp.get_context('spawn')
    f=cxt.Value('i', 0)
    p=cxt.Process(target=demo, args=[f])
    p.start()

    return p

if __name__ == "__main__":
    p=main()
    p.join()
