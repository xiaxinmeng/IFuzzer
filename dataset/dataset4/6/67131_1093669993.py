# Why is this wrong?
print(1,2,)     # is allowed
print(*(1,2))   # is allowed
#print(*(1,2),) # is allowed according to the syntax - but not accepted