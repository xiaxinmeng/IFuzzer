from socket import gethostbyaddr, herror as socket_host_error

def ip2name(addr):
    try:
        if addr in ip2name.cache:
            return ip2name.cache[addr]
        name = gethostbyaddr(addr)[0]
    except (socket_host_error, KeyboardInterrupt, ValueError):
        name = addr
    ip2name.cache[addr] = name
    return name
ip2name.cache = {}