import urllib
url = "ftp://ftp.fu-berlin.de/pub/misc/movies/database/ratings.list.gz"
fp = urllib.urlopen(url)
fp.close()  # hangs