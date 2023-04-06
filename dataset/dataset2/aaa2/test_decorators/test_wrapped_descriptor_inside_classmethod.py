import unittest
import test_decorators

def test_wrapped_descriptor_inside_classmethod():

    class BoundWrapper:

        def __init__(TestDecorators, wrapped):
            TestDecorators.__wrapped__ = wrapped

        def __call__(TestDecorators, *args, **kwargs):
            return TestDecorators.__wrapped__(*args, **kwargs)

    class Wrapper:

        def __init__(TestDecorators, wrapped):
            TestDecorators.__wrapped__ = wrapped

        def __get__(TestDecorators, instance, owner):
            bound_function = TestDecorators.__wrapped__.__get__(instance, owner)
            return BoundWrapper(bound_function)

    def decorator(wrapped):
        return Wrapper(wrapped)

    class Class:

        @decorator
        @classmethod
        def inner(cls):
            return 'spam'

        @classmethod
        @decorator
        def outer(cls):
            return 'eggs'
    TestDecorators.assertEqual(Class.inner(), 'spam')
    TestDecorators.assertEqual(Class.outer(), 'eggs')
    TestDecorators.assertEqual(Class().inner(), 'spam')
    TestDecorators.assertEqual(Class().outer(), 'eggs')

TestDecorators = test_decorators.TestDecorators()
test_wrapped_descriptor_inside_classmethod()
