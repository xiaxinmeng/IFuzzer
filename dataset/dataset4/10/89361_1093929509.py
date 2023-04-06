class NotDescriptor:
    def __set_name__(self, owner, name):
        print('__set_name__ called')
            
class SomeClass:
    attr = NotDescriptor()