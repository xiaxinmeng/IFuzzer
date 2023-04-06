class A:
    _name = 'AA'
    def __init__(self,name):
        self._name = name
    def __eq__(self,a):
        if (a._name == self._name):
            return 1
        else:
            return 0
    def __str__(self):
        return self._name

a = A('abc')

c = {}