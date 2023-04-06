def _match_test(test):
    global match_tests
                                                                                                   
    if match_tests is None:
        return True 
    test_id = test.id()                                                                            
                
    for match_test in match_tests:
        if fnmatch.fnmatchcase(test_id, match_test):                                               
            return True
                                                                                                   
        for name in test_id.split("."):                                                            
            if fnmatch.fnmatchcase(name, match_test):                                              
                return True
    return False