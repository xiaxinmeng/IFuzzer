f.seek(0)

f.readline()
print(f.tell())  # output 5 (xxx\r\n)

f.seek(f.tell())

x = f.truncate()
print(x)  # output 5