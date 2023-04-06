import os
with open("x", "w") as f:
    f.write("xxx")
fd = os.open("x", os.O_RDONLY | os.O_APPEND)
print(os.lseek(fd, 0, 1))