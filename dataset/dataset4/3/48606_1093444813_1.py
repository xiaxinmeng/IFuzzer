def CategorizeLine(line, mapping):
   loc = bisect.bisect([m[0] for m in mapping], line)
   if loc == 0:
      return None # before first chunk
   return mapping[loc-1][1]