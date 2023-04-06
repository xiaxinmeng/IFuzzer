from multiprocessing import Pool
import traceback

class Utils:
    def __init__(self):
       self.count = 10

def function():
    global u1
    u1 = Utils()
    l1 = range(3)
    process_pool = Pool(1)
    try:
        process_pool.map(add, l1, 1)
        process_pool.close()
        process_pool.join()
    except Exception as e:
        process_pool.terminate()
        process_pool.join()
        print(traceback.format_exc())
        print(e)

def add(num):
     total = num + u1.count
     print(total)

if __name__ == "__main__":
    function()