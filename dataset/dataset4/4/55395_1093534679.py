def isUndecodableFilename(filename):
  return any((0xDC80 <= ord(ch) <= 0xDCFF) for ch in filename)