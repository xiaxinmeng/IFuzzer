def testme():
    err = Exception("nothing worked")
    try:
        raise ValueError("no value")
    except ValueError as err:
        pass
    print(err)

testme()