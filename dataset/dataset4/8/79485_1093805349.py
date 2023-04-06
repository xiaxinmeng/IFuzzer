f.seek(0)

f.readline()
print(f.tell())  # output 5 (xxx\r\n)

x = f.truncate()
print(x)  # output 13 (xxx\r\nyyy\r\nzzz), why it is 13, not 5?