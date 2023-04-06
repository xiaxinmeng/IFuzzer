import unittest
import test_opcache

def test_descriptor_added_after_optimization():

    class Descriptor:
        pass

    class C:

        def __init__(TestLoadAttrCache):
            TestLoadAttrCache.x = 1
        x = Descriptor()

    def f(o):
        return o.x
    o = C()
    for i in range(1025):
        assert f(o) == 1
    Descriptor.__get__ = lambda TestLoadAttrCache, instance, value: 2
    Descriptor.__set__ = lambda *args: None
    TestLoadAttrCache.assertEqual(f(o), 2)

TestLoadAttrCache = test_opcache.TestLoadAttrCache()
test_descriptor_added_after_optimization()
