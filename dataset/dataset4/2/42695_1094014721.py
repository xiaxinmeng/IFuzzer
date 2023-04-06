def get_bound_nl_sock(netlink_family):
    net_fd = socket.socket(socket.AF_NETLINK,
                           socket.SOCK_RAW,           
     
                           netlink_family)
        
    net_fd.bind((os.getpid(),0))
    return net_fd