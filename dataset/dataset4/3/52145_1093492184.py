def parameterised_test_info(name, cases):
    for idx, case in enumerate(cases, start=1):
        yield ("{}_{}".format(name, idx), case)