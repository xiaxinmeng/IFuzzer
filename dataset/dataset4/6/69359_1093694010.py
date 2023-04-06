@skipIf(crypt)
class TestWhyCryptDidNotImport(TestCase):
    ...

@skipUnless(crypt)
class CryptTestCase(TestCase):
    ...