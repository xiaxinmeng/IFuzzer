# always log ResourceWarning messages
warnings.simplefilter("always", ResourceWarning)
def func():
    f = open(__file__)
    # emit ResourceWarning
    f = None
func()