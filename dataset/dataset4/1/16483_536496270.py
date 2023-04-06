
from enum import Flag
F = Flag("F", list("abcdefghijklm"))
for idx in range(2**len(F) - 1):
    F(idx)
