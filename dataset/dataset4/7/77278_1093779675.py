@atexit.register
def fun():
   pool.submit(print, "apple")