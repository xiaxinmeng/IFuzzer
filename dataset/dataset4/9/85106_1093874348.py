from multiprocessing import Pool,Manager
import time

def f(x):
    cv,t=x
    cv.acquire()
    print(t,"Got cv")
    return 

if __name__ == '__main__':
    m=Manager()
    cv=m.Condition(m.RLock())
    p = Pool(5)
    print(p.map(f, [ (cv,x) for x in range(10) ]))