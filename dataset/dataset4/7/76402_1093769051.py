
In[1]: socket.getnameinfo(('fe80::941f:f6ff:fe04:c560%qwe', 42133, 0, 78), socket.NI_NUMERICHOST)
Out[1]: ('fe80::941f:f6ff:fe04:c560%qwe', '42133')
In[2]: socket.getnameinfo(('fe80::941f:f6ff:fe04:c560', 42133, 0, 78), socket.NI_NUMERICHOST)
Out[2]: ('fe80::941f:f6ff:fe04:c560%qwe', '42133')
