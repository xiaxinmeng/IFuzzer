import imp

class BadSpec:
    name = 42
    origin = 'foo'

imp.create_dynamic(BadSpec())