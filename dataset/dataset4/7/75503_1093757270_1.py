def my_namespace_copy(namespace):
    '''Recursively deep copies nested namespaces'''
    new_NS=SimpleNamespace(**namespace.__dict__.copy())
    for i in new_NS.__dict__.keys():
        if(type(new_NS.__dict__[i]) == types.SimpleNamespace):
            new_NS.__setattr__(i, my_namespace_copy(new_NS.__getattribute__(i)))
    return new_NS