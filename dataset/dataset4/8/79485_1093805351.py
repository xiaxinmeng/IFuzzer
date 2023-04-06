# Code snippet 1
f = open('test', "w+")
f.write('xxx\nyyy\nzzz')

f.seek(0)

f.readline()
print(f.tell())  # 5

x = f.truncate()
print(x)  # 13 - why it is 13, not 5?


# Code snippet 2
f = open('test', "w+")
f.write('xxx\nyyy\nzzz')

f.seek(0)

f.readline()
print(f.tell())  # 5

f.seek(f.tell())

x = f.truncate()
print(x)  # 5