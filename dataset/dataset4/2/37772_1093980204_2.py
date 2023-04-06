bslc = b[x:]  # take slice of array starting at x
bslc[0] += c   #  add c to b[x] 
a = bslc[0]    # and copy to a without evaluating x twice