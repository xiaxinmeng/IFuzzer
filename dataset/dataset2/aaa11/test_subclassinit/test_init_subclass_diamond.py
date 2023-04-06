import types
import unittest
import test_subclassinit

def test_init_subclass_diamond():

    class Base:

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.calls = []

    class Left(Base):
        pass

    class Middle:

        def __init_subclass__(cls, middle, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.calls += [middle]

    class Right(Base):

        def __init_subclass__(cls, right='right', **kwargs):
            super().__init_subclass__(**kwargs)
            cls.calls += [right]

    class A(Left, Middle, Right, middle='middle'):
        pass
    Test.assertEqual(A.calls, ['right', 'middle'])
    Test.assertEqual(Left.calls, [])
    Test.assertEqual(Right.calls, [])

Test = test_subclassinit.Test()
test_init_subclass_diamond()
