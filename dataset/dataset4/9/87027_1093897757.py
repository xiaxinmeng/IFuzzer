v4 = IPv4Network("10.10.0.72/30")
next_network = v4.next_subnet(next_prefix=30)
# Output: next_network = IPv4Network("10.10.0.76/30")

v4 = IPv4Network("10.10.0.72/30")
next_network = v4.next_subnet() # if next_prefix is not defined it will use the existing prefix of /30, so this call is exactly the same as the previous
# Output: next_network = IPv4Network("10.10.0.76/30")

v6 = IPv6Network("2001:db8:aaaa:aaaa:aaaa:aaaa:aaaa:0000/112")
next_network = v6.next_subnet()
# Output: next_network = IPv6Network("2001:db8:aaaa:aaaa:aaaa:aaaa:aaab:0/112")

v6 = IPv6Network("2001:db8:aaaa:aaaa:aaaa:aaaa:aaaa:0000/112")
next_network = v6.next_subnet(next_prefix=64)
# Output: next_network = IPv6Network("2001:db8:aaaa:aaab::/64")