if test_runner is None:
    def test_runner():
        tests = unittest.TestLoader().loadTestsFromModule(the_module)
        support.run_unittest(tests)
test_runner()