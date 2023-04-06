class Env(dict):
    def __init__(self, external_storage):
        super().__init__()
        self._external_storage = external_storage

    def __setitem__(self, key, value):
        print('__setitem__: {}'.format(key))
        self._external_storage[key] = value

    def __getitem__(self, key):
        print('__getitem__: {}'.format(key))
        return self._external_storage[key]


storage = {}
env = Env(storage)
env['var'] = 2