f = open("a.tar", "rb+")
f.seek(100)
f.write("0"*200)