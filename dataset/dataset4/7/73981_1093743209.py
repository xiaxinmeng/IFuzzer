from multiprocessing import Process, Queue
q = Queue()

def f():
    q.put([42, None, 'hello'])

def main():
    p = Process(target=f)
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()

if __name__ == '__main__':
    main()