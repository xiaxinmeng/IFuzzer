import xmlrpc.client

# create a ServerProxy with an invalid URI
proxy = xmlrpc.client.ServerProxy("http://invalidaddress/")