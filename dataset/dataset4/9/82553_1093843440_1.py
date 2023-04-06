
def test(d: dict): 
     for i in d: 
         d[i+'x'] = d.pop(i)
