from xmlrpclib import Transport, ServerProxy

class MyTransport(Transport):
    def getparser(self):
        parser, unmarshaller = Transport.getparser(self)

        # Get the class attribute, clone it
        dispatch = unmarshaller.dispatch.copy()
        # and store it on the instance
        unmarshaller.dispatch = dispatch