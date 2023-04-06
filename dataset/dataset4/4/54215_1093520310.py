print("in type's dir" , '__abstractmethods__' in dir(type))
print(type.__abstractmethods__)

class type3(type):
    pass

print("in type3's dir" , '__abstractmethods__' in dir(type3))
print(type3.__abstractmethods__)