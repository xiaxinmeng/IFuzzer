def create_server(address, *, 
                  family=AF_INET,        # either AF_INET or AF_INET6 
                  type=SOCK_STREAM,      # either SOCK_STREAM or SOCK_DGRAM
                  backlog=None,          # ignored for type=SOCK_DGRAM
                  reuse_port=False, 
                  dualstack_ipv6=False   # ignored for type=SOCK_DGRAM
):
    ...

def supports_dualstack_ipv6():
    ...