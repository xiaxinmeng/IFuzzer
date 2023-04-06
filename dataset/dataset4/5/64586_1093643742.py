s =b"if False:\n\tx=3\n\ty=3\n"
t = tokenize(io.BytesIO(s).readline)
for i in t: print(i)