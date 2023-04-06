it = chain("ab", "cd")
throw_away = next(it)
assert len(it) == 2 + 2  # call len() on the sequences
assert len(list(it)) == len(it)  # fails since 3 != 4