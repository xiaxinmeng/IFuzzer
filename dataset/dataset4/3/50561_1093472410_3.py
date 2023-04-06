import urllib2

class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'

url = 'http://www.youtube.com/watch?v=tCVqx2b-c7U'
# Note: I had this problem with this URL, the video 
# is not available in my country (Finland) and it
# may work fine for other countries

req = HeadRequest(url)
page = urllib2.urlopen(req)