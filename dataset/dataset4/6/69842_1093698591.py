import urllib2 
from multiprocessing.dummy import Pool as ThreadPool

def start_multithreading_urlopen(threads_num):

    pool = ThreadPool(threads_num)
    results = pool.map(urllib2.urlopen, [])
    pool.close() 
    pool.join()