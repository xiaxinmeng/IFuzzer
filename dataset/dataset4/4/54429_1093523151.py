def getgeneratorstate(g):
  if g.gi_running:
    return GEN_RUNNING
  if g.gi_frame is None:
    return GEN_CLOSED
  if g.gi_frame.f_lasti == -1:
    return GEN_CREATED
  return GEN_SUSPENDED