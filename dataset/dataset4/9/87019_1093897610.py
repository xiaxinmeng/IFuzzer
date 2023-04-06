
import http.client
connection = http.client.HTTPSConnection("mirror.aarnet.edu.au")
connection.request("GET", "/pub/centos/8/isos/x86_64/CentOS-8.3.2011-x86_64-dvd1.iso")
response = connection.getresponse()
data = response.read()
