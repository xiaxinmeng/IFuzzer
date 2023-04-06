def blocks(name, size=8192):
   f = open(name, "rb")
   while True:
      data = f.read(size)
      if data:
         yield data
      else:
         break

def decode(it, encoding, errors):
   reader = codecs.getreader(encoding)(None, errors)
   for data in it:
      yield reader.feed(data)

decode(blocks("foo.xml"))