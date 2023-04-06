import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Python-urllib/3.3')]
fobj = opener.open('http://en.wikipedia.org/robots.txt')
print(fobj.getcode())