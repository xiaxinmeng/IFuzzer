import os, concurrent.futures

def parallel_callback( arg ):
    return os.getpid()

def parallel( *args ):
    def thread_callback( param ):
        with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
            future = executor.submit( parallel_callback, param )
            pid = future.result()
            print( 'pid:', pid )
            return pid
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(args)) as executor:
        future = executor.map( thread_callback, args )
        results = list(future)
    print( 'DONE' )

parallel( 1, 2, 3 )