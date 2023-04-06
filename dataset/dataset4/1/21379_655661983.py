# In test/test_inspect.py:849
def test_argspec_api_ignores_wrapped(self):
    # Issue 20684: low level introspection API must ignore __wrapped__
    @functools.wraps(mod.spam)
    def ham(x, y):
        pass
    # Basic check
    self.assertArgSpecEquals(ham, ['x', 'y'], formatted='(x, y)')  # <--- this what fails