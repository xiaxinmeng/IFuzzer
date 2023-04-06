def test_without_exception(self):
    err = traceback.format_exception_only(None, None)
    self.assertEqual(err, ['None\n'])