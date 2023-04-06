from dataclasses import dataclass
from unittest import TestCase


class OrderedDataclassTestCase(TestCase):

    def test_lt(self):
        with self.assertRaises(TypeError):
            @dataclass(order=True)
            class C:
                def __lt__(self, other):
                    return self

    def test_le(self):
        with self.assertRaises(TypeError):
            @dataclass(order=True)
            class C:
                def __le__(self, other):
                    return self

    def test_gt(self):
        with self.assertRaises(TypeError):
            @dataclass(order=True)
            class C:
                def __gt__(self, other):
                    return self

    def test_ge(self):
        with self.assertRaises(TypeError):
            @dataclass(order=True)
            class C:
                def __ge__(self, other):
                    return self