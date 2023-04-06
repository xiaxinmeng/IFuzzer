def betavariate(alpha, beta):
     y = gammavariate(alpha,1)
     if y==0: return 0.0
     else: return  y/(y+gammavariate(beta,1))