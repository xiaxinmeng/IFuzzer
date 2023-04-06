file=open("abcd.txt","w+")
l=["This is python.\nThis is an easy language.\nAnyone can learn this easily"]
file.writelines(l)
file.close()
file=open("abcd.txt","r+")
file.write("123")
t1=file.read()
print(t1)