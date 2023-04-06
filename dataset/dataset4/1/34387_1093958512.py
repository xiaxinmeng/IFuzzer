class MyThreadingHTTPServer(
  SocketServer.ThreadingMixIn,
  MyHTTPServer
):
  def close_request(self, request):
    pass