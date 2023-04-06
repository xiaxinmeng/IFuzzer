with open("x", "w") as f:
    f.write("xxx")
with open("x", "a") as f:
    print(f.tell())