import perf
import re
import binascii
import base64

_B16DECODE_PAT = re.compile(b'[^0-9A-F]')

def b16decode_re_compiled_search(s, casefold=False):
    s = base64._bytes_from_decode_data(s)
    if casefold:
        s = s.upper()
    if _B16DECODE_PAT.search(s):
        raise binascii.Error('Non-base16 digit found')
    return binascii.unhexlify(s)

if __name__ == "__main__":
    hex_data = "806903d098eb50957b1b376385f233bb3a5d54f54191c8536aefee21fc9ba3ca"
    hex_data_upper = hex_data.upper()