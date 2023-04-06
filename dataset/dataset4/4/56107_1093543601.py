f = open("data", "r")
mydata = f.read()
f.close()

#this fails
url=unicode('http://localhost/test')