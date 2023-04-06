from email.FeedParser import FeedParser
parser = FeedParser()
# Create bogus content-type header...
parser.feed('Content-type: %s ; boundary=%s \r\n\r\n' %
(self.type, self.innerboundary))
parser.feed(self.fp.read())
message = parser.close()