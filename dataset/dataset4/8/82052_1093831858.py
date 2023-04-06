# There is no error if N = 472 or 474.
N = 473
# There is no error if W = 39 or 41.
# (I tested with console windows of varying sizes, all well over 40 characters.)
W = 40
# There is no error if ch = "e" with no accent.
# There is still an error for other unicode characters like "Ö" or "ü".
ch = "é"
# There is no error without newlines.
s = (ch * W + "\n") * N
# Assert the string itself is correct.
assert all(c in (ch, "\n") for c in s)
print(s)