import ssl
pem = ssl.get_server_certificate(('svn.python.org', 443), ca_certs="Lib/test/https_svn_python_org_root.pem")
print("PEM: %r" % pem)