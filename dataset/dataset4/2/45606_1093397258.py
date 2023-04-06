# pdbtest.py
import pdb
pdb.set_trace()
print("before with")
with open("/etc/passwd") as fd:
    data = fd.read()
print("after with")
print("end of program")