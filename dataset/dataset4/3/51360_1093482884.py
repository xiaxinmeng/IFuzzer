def test_no_stdin(self):
    out, err = self._test_with_closed_streams(['stdin'])
    [...]

def test_no_streams(self):
    out, err = self._test_with_closed_streams(['stdin', 'stdout', 'stderr'])
    [...]