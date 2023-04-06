import time, sys

# first arg is an ID. Second arg is how long to work in seconds
sys.stdout.write("start slave %s\n" % sys.argv[1])
sys.stdout.flush()

time.sleep(int(sys.argv[2]))

sys.stdout.write("finish slave %s\n" % sys.argv[1])
sys.stdout.flush()