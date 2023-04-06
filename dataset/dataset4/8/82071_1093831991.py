
try:
    self.assertEqual(getattr(module, var), 1)
except AttributeError:
    self.fail(f"{module} should have attribute {var}")
