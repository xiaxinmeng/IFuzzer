
import urlparse as urllib_parse
url = u'example.com\uFF03@bing.com'
url = u'http://\u30d5\u309a\ufe1380'
urllib_parse.urlsplit(url)
