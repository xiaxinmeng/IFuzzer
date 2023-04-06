from http.client import HTTPSConnection
conn = HTTPSConnection("cinnamon-spices.linuxmint.com")
headers = {  # Same header fields sent by “urllib.request”
    "Accept-Encoding": "identity",
    "Host": "cinnamon-spices.linuxmint.com",
    "User-Agent": "Python-urllib/3.6",
    "Connection": "close",
}
conn.request("GET", "/json/applets.json", headers=headers)
resp = conn.getresponse()
print(resp.msg)
data = resp.read()