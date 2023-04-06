from unittest.mock import create_autospec

class DummyClass:
    pass

dummy_class = create_autospec(DummyClass)
dummy_class.a