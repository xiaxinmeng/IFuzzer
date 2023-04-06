def chunk(block):
   return hex(len(block)).encode('ascii') + b'\r\n' + block + b'\r\n'