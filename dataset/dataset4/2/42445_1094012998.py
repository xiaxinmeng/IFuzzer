# Fix missing Apple logo in mac_roman.
import encodings.mac_roman
if not encodings.mac_roman.decoding_map[0xF0]:
    encodings.mac_roman.decoding_map[0xF0] = 0xF8FF
    encodings.mac_roman.encoding_map[0xF8FF] = 0xF0