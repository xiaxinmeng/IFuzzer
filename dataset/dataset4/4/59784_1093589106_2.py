utemplist = copy.copy(uzlist)
for i in range(len(uzlist)):
   try: 
     if utzdict[ uzlist[i] ]: utemplist.remove( uzlist[i] )
   except KeyError: pass