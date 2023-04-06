from html.parser import HTMLParser
parser = HTMLParser()
parser.feed(bytearray.fromhex('3c215b63612121').decode('ascii'))