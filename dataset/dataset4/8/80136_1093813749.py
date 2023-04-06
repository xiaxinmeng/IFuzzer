import difflib

for i in range(7):
    print(f"Change character at {i}")
    a = list("drwxrwxr-x 2 2000  2000\n")
    b = "drwxrwxr-x 2 2000  2000\n"
    a[i] = '-'
    a = ''.join(a)
    print(''.join(difflib.ndiff([a], [b])))