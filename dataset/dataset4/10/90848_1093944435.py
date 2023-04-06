
from unittest.mock import create_autospec

class Test:
    def test_method(self):
        pass

autospec_mock = create_autospec(Test, instance=True, **{"test_method.side_effect": ValueError})

# Should throw a ValueError exception
autospec_mock.test_method()

# Assign manually
autospec_mock.test_method.side_effect = ValueError
# Throws as expected
autospec_mock.test_method()
