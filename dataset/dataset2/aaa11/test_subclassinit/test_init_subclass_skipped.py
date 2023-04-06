import types
import unittest
import test_subclassinit

def test_init_subclass_skipped():

    class BaseWithInit:

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.initialized = cls

    class BaseWithoutInit(BaseWithInit):
        pass

    class A(BaseWithoutInit):
        pass
    Test.assertIs(A.initialized, A)
    Test.assertIs(BaseWithoutInit.initialized, BaseWithoutInit)

Test = test_subclassinit.Test()
test_init_subclass_skipped()
