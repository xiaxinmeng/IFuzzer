class Base:
    def __init_subclass__(cls):
        global broken_class
        broken_class = cls
        assert 0
try:
    class Broken(Base): pass
except: pass
assert broken_class not in Base.__subclasses__()