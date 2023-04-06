mess_with_ref_count() # In 3rd party code
non_3rd_party_code() #the error may occur here, after the refcount was messed with, and gdb will show this function in the stack trace