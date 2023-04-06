
#!/usr/bin/env python3

import multiprocessing

def check_child(q):
    print("Queue", q)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    # multiprocessing.set_start_method('fork')
    # multiprocessing.set_start_method('forkserver')

    q = multiprocessing.Queue(-1)
    print("q", q)

    proc = multiprocessing.Process(target=check_child, args=(q,))
    proc.start()
