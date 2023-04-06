from xml.etree.ElementTree import Element, tostringlist, tostring

element = Element("foo")
print ("".join(tostringlist(element)) == tostring(element))