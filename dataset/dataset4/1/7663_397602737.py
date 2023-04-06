
import sys, os
sys.stdout.write("hello")
sys.stdout.flush()
os.fsync(sys.stdout.fileno())
