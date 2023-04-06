

def wrapper(*args, **kwargs):
    return MockError(*args, **kwargs)

patcher = patch('__main__.ProductionError', side_effect=wrapper)

