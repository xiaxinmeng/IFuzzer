def findtestclasses(mod):
    tests = []
    for elem in dir(mod):
        member = getattr(mod, elem)
        if type(member) != type: continue
        if issubclass(member, unittest.TestCase):
            tests.append(member)
    return tests