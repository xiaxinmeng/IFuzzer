def isUndecodableFilename(filename):
  return any((0xD800 <= ord(ch) <= 0xDFFF) for ch in filename)