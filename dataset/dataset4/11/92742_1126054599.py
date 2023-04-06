
def adapter_func(obj):
    return pickle.dumps(obj, protocol=0).decode('utf-8')

def converter_func(data):
    return pickle.loads(data.encode('utf-8'))
