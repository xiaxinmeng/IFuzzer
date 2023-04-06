# defined near top of module:
MapCRLF = re.compile(r'\r\n|\r|\n')

# in append method:
self.literal = MapCRLF.sub(CRLF, message)