# APIKEY defined above
r = urllib.request.urlopen('http://api.billboard.com/apisvc/chart/v1/'
                           'list/spec?api_key={}&format=JSON'
                           .format(APIKEY))
j = json.load(r)