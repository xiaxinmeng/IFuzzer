import os, sys
environb = {os.fsencode(k):os.fsencode(v) for k,v in os.environ.items()}
os.spawnve(os.P_WAIT, sys.executable, ('python', '--version'), environb)
