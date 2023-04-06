import urllib.request
import ssl
https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv3))
opener = urllib.request.build_opener(https_sslv3_handler)
urllib.request.install_opener(opener)
urllib.request.urlopen('https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.P_GetCrse')