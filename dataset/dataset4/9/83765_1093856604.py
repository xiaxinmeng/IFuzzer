
from multiprocessing.shared_memory import SharedMemory
shm = SharedMemory(name='test-crash', create=True, size=1000000000000000000)
