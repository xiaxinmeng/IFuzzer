# Python asks the OS to open a new file. The OS puts the new file on
# the list and gives it the lowest number that is not in use: 3.
fd = tempfile.TemporaryFile()
# fd is an file object for file no 3
with open(fd.fileno()) as f:
    # f is another object for file no 3
    pass             # I know fd is closed after with is done
# the with statement closes file no 3
# fd does not know that file no 3 is closed. (and has no way of knowing!)

# Python asks the OS to open a new file. The OS puts the new file on
# the list and gives it the lowest number that is not in use: 3.
_tmp = tempfile.TemporaryFile()
# A new temporary file object is created for file no 3
fd = _tmp
# The old fd is finalized. It still thinks it has control of file
# no 3, so it closes that. The new temporary file object is given
# the name fd.