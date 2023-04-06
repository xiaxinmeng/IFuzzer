import xmlrpclib
e = xmlrpclib.Fault("Error", "Message")
((d,), _) = xmlrpclib.loads(xmlrpclib.dumps((e,)))
assert d['faultString'] == "Message"