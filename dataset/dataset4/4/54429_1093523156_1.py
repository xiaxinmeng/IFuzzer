def getgeneratorstate(g):
  """Get current state of a generator-iterator.
  
  Possible states are:
    GEN_CREATED: Waiting to start execution
    GEN_RUNNING: Currently being executed by the interpreter
    GEN_SUSPENDED: Currently suspended at a yield expression
    GEN_CLOSED: Execution has completed
  """