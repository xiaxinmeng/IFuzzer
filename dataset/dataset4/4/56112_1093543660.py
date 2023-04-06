class ModuleLevelMiscTest(BaseTest):
    [...]
    def _test_log(self, method, level=None):
        called = []
        patch(self, logging, 'basicConfig',
              lambda *a, **kw: called.append(a, kw))  # <