
import sys
import _cpp
message = _cpp.ReadSharedMemory(shared_mem_agent, 0)
print(sys.getrefcount(message))
