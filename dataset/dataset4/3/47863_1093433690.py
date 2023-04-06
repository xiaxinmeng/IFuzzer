import xmlrpc.client
transp = xmlrpc.client.Transport()
transp.get_host_info("user@host.tld")