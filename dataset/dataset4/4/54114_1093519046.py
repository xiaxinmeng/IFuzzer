import subprocess, os

os.close(0) # Works correctly if any of these two are commented out.
os.close(2)