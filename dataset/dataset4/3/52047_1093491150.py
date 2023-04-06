def load_tests(loader, standard_tests, pattern):
    for case in email.test.emailtestdb.populated_test_cases(globals()):
        standard_tests.addTests(loader.loadFromTestCase(case))
    return standard_test