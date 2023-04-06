zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
# user *MUST* call zk.stop() otherwise there is a leak