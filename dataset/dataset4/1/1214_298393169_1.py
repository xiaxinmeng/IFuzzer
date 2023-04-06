
if "\nPORT" in line.upper():
      raise ValueError("malicious PORT injection %r" % line)
