def str_width(s):
  width=1
  for ch in map(ord,s):
    if ch > 0xFFFF: return 4
    if ch > 0xFF: width=2
  return width