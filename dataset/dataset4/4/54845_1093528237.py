import signal
import subprocess

to_launch = None

def sig_chld_handler(signum, frame):
    global to_launch
    # Crashes here.
    # 'NoneType' object has no attribute 'poll'
    to_launch.poll()