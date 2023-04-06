def str_width(s):
  width=1
  for ch in map(ord,s):
    if n > 0xFFFF: return 4
    if n > 0xFF: width=2
  return width