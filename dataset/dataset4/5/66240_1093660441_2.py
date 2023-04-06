import http.client, urllib.parse
data = urllib.parse.urlencode({'QLastname': 'DIAZ HERNANDEZ', 'QFirstname': 'JAIME'})
headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/plain"}
conn = http.client.HTTPConnection(proxy_url,8080, source_address=(ipAddress, 0))
conn.set_tunnel("www.infobel.com")
conn.request("POST", "/es/spain/people.aspx", data, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()