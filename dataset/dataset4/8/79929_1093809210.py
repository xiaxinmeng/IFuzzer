
from urllib.parse import urlparse
x= 'http://www.google.com\@xxx.com'
y = urlparse(x)
print(y.hostname)
