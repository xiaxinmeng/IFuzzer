f = open('data.txt', 'w')
f.write("""line 1
line 2
line 3
line 4
line 5
line 6
line 7
line 8
line 9
line 10
line 11
""")
f.close()


f = open('data.txt', 'r')
assert f.readline() == 'line 1\n'