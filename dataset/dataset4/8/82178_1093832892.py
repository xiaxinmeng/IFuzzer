
def CreateDynamicClass(basetype):
    class DynamicClassImpl(basetype):
        def __init__(self):
            super(DynamicClassImpl, self).__init__()
    
    return DynamicClassImpl()

# Comment out any of the following three lines and the test passes
dynamic_memerror = CreateDynamicClass(MemoryError)
memory_error = MemoryError("Test")
dynamic_memerror = CreateDynamicClass(MemoryError)

print(MemoryError("Test2"))
