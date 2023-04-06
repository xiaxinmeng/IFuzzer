class A(object):
  def __len__(self): 
    return -2  # anything < 0

  def __getslice__(self, x, y):  
    pass