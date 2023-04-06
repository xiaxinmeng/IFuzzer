from unittest.mock import Mock, patch
from unittest import TestCase, main


class Foo:
    properties = []


class FooTest(TestCase):
    def setUp(self):
        patcher = patch(f"{__name__}.Foo.properties", new_callable=list)
        self.addCleanup(patcher.stop)
        patcher.start()

    def test_foo(self):
        Foo.properties.append(1)
        self.assertEqual(Foo.properties, [1])

    def test_bar(self):
        Foo.properties.append(2)
        self.assertEqual(Foo.properties, [2])


if __name__ == "__main__":
    main()