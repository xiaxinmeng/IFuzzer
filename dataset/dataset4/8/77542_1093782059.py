
b = io.BytesIO(u'a,b\r\n"asdf","jkl;"\r\n'.encode('ibm500'))
s = codecs.EncodedFile(b, 'ibm500')
