a = array.array('I')
a.fromstring('\x01\x02\x03\x04')
print(a)
#array('I', [67305985L])  # one element as expected (4 bytes, 4 bytes/elt)

a = array.array('H')
a.fromstring('\x01\x02\x03\x04')
print(a)
#array('H', [513, 1027])  # two elements as expected (4 bytes, 2 bytes/elt)