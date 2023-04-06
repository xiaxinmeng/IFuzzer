class OperatorTestsMixin:
    module = None

class COperatorTests(OperatorTestsMixin, unittest.TestCase):
    module = _operator