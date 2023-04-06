tmp = zipfile.ZipFile("tmp.zip", mode="w")
import io
x = io.BytesIO("hello world!".encode("utf-8"))
tmp.writestr("helloworld.txt", x.getbuffer())
tmp.close()