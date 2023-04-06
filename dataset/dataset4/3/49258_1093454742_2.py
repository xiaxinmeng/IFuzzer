with open("x", "w") as f:
    f.write("xxx")
with open("x", "a") as f:
    f.write("y")
    print(f.tell())