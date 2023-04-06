   
def setunion(x,y):
      l=len(y)
      p=x
      for j in range(0,l):
          z=y.pop(0)
          y.append(z)
          if(p.count(z)==0):
               p.append(z)
      return(p)