def tracer(*args):
  print("trace")
  return tracer
import sys
sys.settrace(tracer)
