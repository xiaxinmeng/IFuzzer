part1 = 'Content-Type: multipart/related; start=<op.mhtml.1247227666422.e6e72d4c344a2503@192.168.1.20>; boundary=----------1JBOHhxKNnWgkmE17ZJ2Cy\r\nContent-Location: http://localhost/page1.html\r\nSubject: =?utf-8?Q?test?=\r\nMIME-Version: 1.0\r\n\r\n------------1JBOHhxKNnWgkmE17ZJ2Cy\r'
part2 = '\nContent-Disposition: inline; filename=page1.html\r\nContent-Type: text/html; charset=UTF-8; name=page1.html\r\nContent-Id: <op.mhtml.1247227666422.e6e72d4c344a2503@192.168.1.20>\r\nContent-Location: http://localhost/page1.html\r\nContent-Transfer-Encoding: 8bit\r\n\r\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html><head><title>Page 1</title></head><body><p>page 1</p></body></html>\r\n------------1JBOHhxKNnWgkmE17ZJ2Cy--\r\n'
expected = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html><head><title>Page 1</title></head><body><p>page 1</p></body></html>'
from email.feedparser import FeedParser
feedparser = FeedParser()
feedparser.feed(part1)
feedparser.feed(part2)
m = feedparser.close()
mm = m.get_payload()
mm[0].get_payload() == expected