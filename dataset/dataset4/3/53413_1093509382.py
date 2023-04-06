text = (
  b'\xff'         # invalid byte
  b'\xc3\xa9'     # valid utf-8 character
  b'\xc3\xff'     # invalid byte sequence
  b'\xed\xa0\x80' # lone surrogate character (invalid)
)