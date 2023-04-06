z = zipfile.ZipFile("data.zip", 'r')
z.setpassword("aafy")
print(z.read("secretfile.txt"))