import multiprocessing
import ctypes

def child_process_fun(share):
    share.value = 'bb'

if __name__ == '__main__':
    share = multiprocessing.Value(ctypes.c_wchar_p, 'aa')
    process = multiprocessing.Process(target=child_process_fun, args=(share, ))
    process.start()
    process.join()
    print(share.value)