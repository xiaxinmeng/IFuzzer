def test_isabstract_during_init_subclass(self):
    from abc import ABCMeta, abstractmethod

    isabstract_checks = []

    class AbstractChecker(metaclass=ABCMeta):
        def __init_subclass__(cls):
            abstract_checks.append(inspect.isabstract(cls))

    class AbstractClassExample(AbstractChecker):

        @abstractmethod
        def foo(self):
            pass

    class ClassExample(AbstractClassExample):
        def foo(self):
            pass

    self.assertEqual(isabstract_checks, [True, False])