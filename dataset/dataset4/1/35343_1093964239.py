import xmlrpclib
m = xmlrpclib.Marshaller()
a = ['1']
b = [a,a]
m.dumps(b) 