import readline, rlcompleter
readline.parse_and_bind('tab: complete')
import thread
import math
def starter(a):
  for i in range(1000000):
    a = math.cos(i)

thread.start_new_thread(starter, (1,))