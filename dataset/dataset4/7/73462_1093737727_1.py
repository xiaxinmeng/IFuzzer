from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
parser = MyHTMLParser()
parser.feed('<a href="http://somesite.com/large_image.jpg"><img src="http://somesite.com/small_image.jpg" width="800px" /></a>')