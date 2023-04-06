from unittest import TestCase, makeSuite, main

class T(TestCase):
    def test_moo(self):
        self.fail()


test_suite = makeSuite(T, "test_")

if __name__ == "__main__":
    main()