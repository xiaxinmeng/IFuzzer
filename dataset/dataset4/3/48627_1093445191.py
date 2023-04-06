def pythonEncoding(filename):
   with open(filename, 'rb') as fp:
      encoding, lines = detect_encoding(fp.readline)
   return encoding