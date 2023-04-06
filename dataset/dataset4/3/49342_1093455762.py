a = 'Something'

def variable_both_global_and_local()->Exception('No good!'):
    del a    # delete a from global name space
    a = 'anotherthing'  # define a in local name space