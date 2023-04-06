transport = Transport()
con = transport.make_connection([host])
con.timeout = 2

proxy = ServerProxy([url], transport=transport)