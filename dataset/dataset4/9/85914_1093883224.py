from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

parser = MyHTMLParser()

#This is ok
parser.feed('<yyy id="poc" a,="">')

#This breaks
parser.feed('<zzz id="poc" ,a="">')

#Future calls to feed() will not work
parser.feed('<img id="poc" src=x>')