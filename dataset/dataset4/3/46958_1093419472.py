def formatTimedelta(delta):
   return "{0}h {1}min {2}sec".format(*str(delta).split(':'))