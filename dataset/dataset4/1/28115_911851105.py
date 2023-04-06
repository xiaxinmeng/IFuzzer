
from supervisor.compat import urllib
...
type, uri = urllib.splittype(serverurl)
host, path = urllib.splithost(uri)
host, port = urllib.splitport(host)
