if __name__ == '__main__':
    mainSuite = TestSuite()
    mainSuite._tests.extend( loadTestsFromPath('.')._tests )
    ttr = TextTestRunner(verbosity=2)
    ttr.run( mainSuite )