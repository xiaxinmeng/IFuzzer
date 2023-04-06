def assert_equal(first, second, msg=None):
    # Implementation could be copied independently of any test state
    TestCase().assertEqual(first, second, msg)