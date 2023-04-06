fd = tempfile.TemporaryFile()
with open(fd.fileno()) as f:
    pass             # I know fd is closed after with is done

fd = tempfile.TemporaryFile() # since tempfile.TemporaryFile() is 
                              # called again, it should return a 
                              # valid file descriptor, and the above 
                              # operations in “with” chunk should
                              # not influence its result

fd.seek(0)   # this should work, however, in reality, it does not