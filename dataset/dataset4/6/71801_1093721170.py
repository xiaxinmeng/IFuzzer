def setUp(self):
    serv = DOCXMLRPCServer(...)
    self.addCleanup(serv.server_close)
    [_, PORT] = serv.server_address  # Eliminates “ready“ event
    # Other server setup here
    thread = threading.Thread(target=serv.serve_forever)
    thread.start()
    self.addCleanup(thread.join)  # Instead of self.evt
    self.addCleanup(serv.shutdown)
    self.client = httplib.HTTPConnection("localhost:%d" % PORT)
    self.addCleanup(self.client.close)