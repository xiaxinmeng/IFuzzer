def f():
  canBusType = 'CANdiag'
  return (eval('canBusType') for i in range(3) if True or canBusType)