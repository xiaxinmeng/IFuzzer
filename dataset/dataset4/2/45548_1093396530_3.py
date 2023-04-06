if __name__ == '__main__':
    mainSuite = TestSuite()
    mainSuite._tests.extend( loadTestsFromPath( 'libvy/tests' )._tests )
    mainSuite._tests.extend( loadTestsFromPath( 'qvy/tests' )._tests )
    mainSuite._tests.extend( loadTestsFromPath( 'tests' )._tests )
    ttr = TextTestRunner(verbosity=2)
    ttr.run( mainSuite )