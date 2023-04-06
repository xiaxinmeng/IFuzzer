_addr_cache = {}

def ipaddr(addr):
    try:
        return _addr_cache[addr]
    except KeyError:
        _addr_cache[addr] = ipaddress.ipaddress(addr)
        return _addr_cache[addr]