class TestProgram(unittest.TestProgram):

    def runTests(self):
        if self.testRunner is None:
            self.testRunner = unittest.TextTestRunner(stream=sys.stdout, verbosity=self.verbosity)
        result = self.testRunner.run(self.test)
        sys.exit(not result.wasSuccessful())

if __name__ == '__main__':
    TestProgram()