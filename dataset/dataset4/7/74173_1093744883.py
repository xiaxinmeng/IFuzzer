test2 = lambda: test(a=10)  # test2() returns a generator

def test(a):
    '''Redefined as a non-generator!'''
# Now test2() returns None