import cProfile
def test():
    import sys
    import dis

with cProfile.Profile() as p:
    test()