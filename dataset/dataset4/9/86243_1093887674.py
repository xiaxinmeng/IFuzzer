
import ssl
import urllib.request

url_string = "https://kubernetes.default.svc.cluster.local./api/"

ctx = ssl._create_unverified_context()

with urllib.request.urlopen(url_string, context=ctx) as f:
    f.read()
