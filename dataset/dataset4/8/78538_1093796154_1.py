import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://cinnamon-spices.linuxmint.com/json/applets.json')
print(response.data)
