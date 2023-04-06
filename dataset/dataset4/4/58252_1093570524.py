import urllib.request
html = urllib.request.urlopen('http://www.basicinstructions.net/').read()
print('Succeeded!')