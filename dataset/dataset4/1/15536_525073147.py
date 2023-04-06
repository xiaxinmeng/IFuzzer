
import unicodedata
for n in range(0x2167, 0x2169):
    print(hex(n), chr(n), unicodedata.name(chr(n)))

# output:
# 0x2167 Ⅷ ROMAN NUMERAL EIGHT
# 0x2168 Ⅸ ROMAN NUMERAL NINE
