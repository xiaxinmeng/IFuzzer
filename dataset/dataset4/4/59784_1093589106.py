import copy

uzlist = [u'abc', u'def', u'ghj', u'klm', u'zxc']
utzdict = {u'abc':1, u'def':2, u'ghj':3, u'klm':4, u'zxc':5}

utemplist = copy.copy(uzlist)
for m in utemplist:
    if m in utzdict.keys(): utemplist.remove(m)