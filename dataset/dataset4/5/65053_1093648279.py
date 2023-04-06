class MyManager(BaseManager): pass
MyManager.register('MyClass', MyClass, method_to_typeid={'get_child':'MyClass'})