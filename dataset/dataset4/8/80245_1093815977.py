import urllib
import urllib.request

my_url = "https://api.foo.com"
my_headers = { "Content-Type" : "application/x-www-form-urlencoded" }
my_data = {
        "client_id" : "ppp",
        "client_secret" : "000",
        "grant_type" : "client_credentials" }

req = urllib.request.Request(url=my_url, data=my_data, headers=my_headers)
response = urllib.request.urlopen(req)
html = response.read()
print(html)