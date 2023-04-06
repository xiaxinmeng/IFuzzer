
def test(d: dict): 
     for i in d: 
         d[i+1] = d.pop(i)
