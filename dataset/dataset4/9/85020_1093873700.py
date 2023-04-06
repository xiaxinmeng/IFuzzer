import os
import tarfile
import time

t0 = time.time()
for tarInfo in tarfile.open( 'sparse.tar', 'r:', ignore_zeros = True ):
    pass
t1 = time.time()
print( f"Small TAR took {t1 - t0}s to iterate over" )

f = open( 'sparse.tar', 'wb' )
f.truncate( 2*1024*1024*1024 )
f.close()

t0 = time.time()
for tarInfo in tarfile.open( 'sparse.tar', 'r:', ignore_zeros = True ):
    pass
t1 = time.time()
print( f"Small TAR with sparse tail took {t1 - t0}s to iterate over" )