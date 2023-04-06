with self.assertRaisesRegex(
        AssertionError,
        re.escape("Error processing expected calls.\n"
                  "Errors: [None, TypeError('too many positional "
                  "arguments')]\n"
                  "Expected: [call(), call('wrong')]")) as cm:
    mock.assert_has_calls([call(), call('wrong')])

with self.assertRaisesRegex(
        AssertionError,
        re.escape("Error processing expected calls.\n"
                  "Errors: [None, TypeError('too many positional "
                  "arguments')]\n"
                  "Expected: [call(), call('wrong')]\n"
                  "Actual: [call()]")) as cm:
    mock()
    mock.assert_has_calls([call(), call('wrong')])
