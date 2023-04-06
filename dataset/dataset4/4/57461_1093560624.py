x = list(accumulate(seq))
assert x == list(accumulate(differences(x)))