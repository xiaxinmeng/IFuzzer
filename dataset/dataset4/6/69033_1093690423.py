def main(namespace):
    for name, obj in namespace.items():
        if name.startswith('test_') and hasattr(obj, '__call__'):
            print(name)
            obj()