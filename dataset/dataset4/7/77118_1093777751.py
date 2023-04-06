# repro.py
import multiprocessing
from multiprocessing import Pool, Manager
import time
import random

def worker_function( index, messages ):

    print( "%d: Entered" % index )
    time.sleep( random.randint( 3, 15 ) )
    messages.put( "From: %d" % index )
    print( "%d: Exited" % index )


def main():
    manager = Manager()
    messages = manager.Queue()
    with Pool( processes = None ) as pool:

        for x in range( 30 ):
            pool.apply_async( worker_function, [ x, messages ] )

        pool.close()
        pool.join()
# EOF