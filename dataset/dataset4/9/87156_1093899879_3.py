import unittest.mock

def func():
    with unittest.mock.patch('builtins.chr', return_value='mock'):
        return chr(65)

print(func())