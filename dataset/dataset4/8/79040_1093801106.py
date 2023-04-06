str2 = open('sample.txt', 'rU').read()


if "\n" in str2:
        print ("\\n found")
else:
        print ("\\n not found")

if "\r" in str2:
        print ("\\r found")
else:
        print ("\\r not found")


if "\r\n" in str2:
        print ("\\r\\n found")
else:
        print ("\\r\\n not found")