class MyHTMLParser(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('got starttag: {0} with attributes {1}'.format(tag, attrs))

    def handle_endtag(self, tag):
        print('got endtag: {0}'.format(tag))