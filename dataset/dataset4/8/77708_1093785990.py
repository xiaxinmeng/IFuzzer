def parent_function2( argument1 ):
        def child_function():
                print( argument1 )
                if False:
                        argument1 = None  # Same function but with fake assignment

        return child_function