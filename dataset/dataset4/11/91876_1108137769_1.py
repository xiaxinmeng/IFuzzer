import time
from Lib.threading import thread


@thread
def count_to(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(1)



t1 = count_to(3)
t2 = count_to(5)
print("done")