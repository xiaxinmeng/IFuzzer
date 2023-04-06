if not filename:
   ct = part.get("Content-Type")
   if ct:
      m = re.compile('name=\"?(\S+)\"?').search(ct, 1)
      if m: filename = m.group(1)