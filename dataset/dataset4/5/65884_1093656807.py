from zipfile import ZipFile, ZIP_DEFLATED
document = '/tmp/example.odt'                     # SET ME PLEASE
S2b, R2b = 'SUBST'.encode(), 'REPLACEMENT'.encode()
with ZipFile(document,'a', ZIP_DEFLATED) as z:
	xmlString = z.read('content.xml')
	xmlString = xmlString.replace(S2b, R2b)
	z.writestr('content.xml', xmlString)