class _TestArray(BaseTestCase):
    [...]
    def test_array(self, raw=False):
        [...]
        p = self.Process(target=self.f, args=(arr,))