import libxml2

file = open("ihanmikavaan.xml", "w")
file.write("<doc>hajoa!</doc>")
file.close()

reader = libxml2.newTextReaderFilename("ihanmikavaan.xml")
reader.Close()

# reading after Close is a seg fault, not an exception
ret = reader.Read()