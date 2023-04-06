mystr  = "hello123"
for x in range(1000000):
    mystr = mystr.__class__
input('>')  # Hit Enter to continue.
del mystr   # Expect crash here.
input('<')  # And never get here