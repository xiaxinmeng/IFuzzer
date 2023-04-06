import ipaddress as ip
a = ip.IPv4Address('0.0.0.42')
a.bits == '0b00000000000000000000000000101010'