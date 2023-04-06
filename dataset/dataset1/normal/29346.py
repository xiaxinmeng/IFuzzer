"""
script printing behavior of utcfromtimestamp() for various bitsizes
"""
import datetime

bits = 30

while bits < 64:
    try:
        result = datetime.datetime.utcfromtimestamp(1<<bits)
        print("{0} {1!r}".format(bits, result))
    except Exception as err:
        print("{0} {1}({2!r})".format(bits, type(err).__name__, str(err)))
    bits += 1

