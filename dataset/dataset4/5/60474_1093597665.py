import urllib.request
import ftplib
ftplib.FTP.debugging = 4
url = "ftp://ftp.fu-berlin.de/pub/misc/movies/database/ratings.list.gz"
with urllib.request.urlopen(url):
    pass