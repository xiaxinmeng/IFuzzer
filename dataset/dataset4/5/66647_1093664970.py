def load_tests(loader, tests, pattern):
    print("HI WE ARE LOADING!")
    this_dir = os.path.dirname(__file__)
    tests.addTest(loader.discover(start_dir=this_dir, pattern=pattern))
    return tests
EOF