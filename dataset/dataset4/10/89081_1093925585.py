from html.parser import HTMLParser

parser = HTMLParser()
parser.feed(bytearray.fromhex('3c215b02634717').decode('ascii'))