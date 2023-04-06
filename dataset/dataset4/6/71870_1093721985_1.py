p = ipaddress.IPv4Network("172.0.0.4/30")
subnets = p.subnets(new_prefix=31)
n = next(subnets)

print(list(n.hosts()))