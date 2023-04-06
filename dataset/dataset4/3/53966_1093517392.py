def _check_released(self, m, tp):
  ...
  self.assertNotEqual(m, memoryview(tp()))
  self.assertNotEqual(m, tp())