import multiprocessing

def f(m):
    print(m)

if __name__ == '__main__':
    p = multiprocessing.Process(target=f, args=('pouet',))
    p.start()
# 