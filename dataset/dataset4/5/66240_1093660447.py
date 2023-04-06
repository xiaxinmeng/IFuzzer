import http.client, urllib.parse
data = urllib.parse.urlencode({'nombre': 'HERVAS INFANTE ALBERTO'})
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection(proxy_url,8080, source_address=(ip_address, 0))
conn.set_tunnel("www.telexplorer.es",port=80)  
conn.request("POST", "/?zone=namwp",data,headers)
response = conn.getresponse()
print("Test 1: TE - ", response.status, response.reason)
data = response.read()
conn.close()