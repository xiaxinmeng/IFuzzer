import multiprocessing,signal,sys
def sproc(x): signal.pause()
for each in range(int(sys.argv[1])):
  multiprocessing.Process(target=sproc, args=(each,)).start()
signal.pause()