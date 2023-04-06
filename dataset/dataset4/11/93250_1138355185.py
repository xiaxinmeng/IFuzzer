import enum
A = enum.IntFlag("A", {"x": 1})
B = enum.IntFlag("B", {"y": 2})
val = A.x | B.y
print(val, type(val))