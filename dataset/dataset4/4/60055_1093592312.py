import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Python-urllib')]
fobj = opener.open('http://en.wikipedia.org/robots.txt')
print('Finished, no traceback here')