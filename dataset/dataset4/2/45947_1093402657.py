p = subprocess.Popen(["convert", "-",  "png:-"],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)

img = open("img_0948.jpg", "rb")
p.stdin.write(img.read())
with open("test", "wb") as f:
    f.write(p.stdout.read())