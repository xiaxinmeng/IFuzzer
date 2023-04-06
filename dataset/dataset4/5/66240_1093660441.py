import http.client, urllib.parse
data = urllib.parse.urlencode({'QLastname': 'DIAZ HERNANDEZ', 'QFirstname': 'JAIME'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("www.infobel.com",80, source_address=("16.19.109.51", 0))
conn.request("POST", "/es/spain/people.aspx", data, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()