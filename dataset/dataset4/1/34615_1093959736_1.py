def relaxedutf8(enc, uni, startpos, endpos, reason, data):
   if uni[startpos:startpos+2] == u"\xc0\x80":
      return (u"\x00", startpos+2)
   else:
      raise UnicodeError(...)