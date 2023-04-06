def test_cm_is_reentrant(self): 
    ignore_exceptions = suppress(Exception) 
    with ignore_exceptions: 
        pass 
    with ignore_exceptions: 
        len(5) 
    with ignore_exceptions: 
        1/0 
        with ignore_exceptions: # Check nested usage 
            len(5)