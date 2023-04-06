# User entered nothing so params = {'screen_name': None, ..more fields}
params = {k: self.request.get(k, None) for k in self.request.GET}

url = "https://api.twitter.com/1.1/friends/ids.json?" + urllib.urlencode(params)