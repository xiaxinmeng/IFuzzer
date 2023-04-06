ipn = ipaddress.ip_network("2a0c:ac10::/32")
prefix = ipn.prefixlen
if ipn.version == 6:
    rest = int((ipn.max_prefixlen - prefix) / 4)
elif ipn.version == 4:
    rest = int((ipn.max_prefixlen - prefix) / 8)
return ipn.network_address.reverse_pointer.split(".", rest)[-1]