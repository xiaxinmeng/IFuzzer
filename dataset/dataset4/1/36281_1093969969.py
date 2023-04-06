server_proxy = ServerProxy(...)
multicall = MultiCall(server_proxy)
multicall.add(2,3)
multicall.get_address("Guido")