def readall(x) :
  url = x.geturl
  x.close()
  try :
    y = urllib.openurl(url)
  except :
    return None
  return y.read()
  

import urllib

urlobj = urllib.urlopen("someurl")
header = urlobj.read(1)
# some other operations

contents = readall(urlobj)