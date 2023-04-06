finder = DocTestFinder(exclude_empty=False)
suite = DocTestSuite(module, test_finder=finder)