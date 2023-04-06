file=open("abcd.txt","w+")
l=["This is python.\nThis is an easy language.\nAnyone can learn this easily"]
file.writelines(l)
file.close()
file=open("abcd.txt","a+")   #Replacing with w+ also doesn't read.
file.write("123")      
t1=file.read()               #This read() does not work.
print(t1)                    #Does not print anything here.
file.close()