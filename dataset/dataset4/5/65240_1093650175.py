from pathlib import Path
a = Path("/a/testpy/cpython/config.log")
b = Path("/b/testpy/cpython/config.log")
c = Path("/a/otherfolder/text.txt")
print(f"a.parents[-2] == b.parents[-2] -> {a.parents[-2] == b.parents[-2]}") # False
print(f"a.parents[-2] == c.parents[-2] -> {a.parents[-2] == c.parents[-2]}") # True 
# index = -2 because -1 is "/"