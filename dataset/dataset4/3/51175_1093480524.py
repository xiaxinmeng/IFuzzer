if hasattr(sys, 'getwindowsversion'):
  if sys.getwindowsversion() >= (5,1):
    assert hasattr(socket, 'IPPROTO_IPV6')