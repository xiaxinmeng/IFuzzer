u = urllib.request.urlopen('https://www.google.com', context=ctx)
data = u.read()