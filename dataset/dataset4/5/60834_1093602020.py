class Broken:
    def __getattr__(self, name):
        raise Exception('Broken __getattr__')

brocken = Broken()
test('brocken', '')