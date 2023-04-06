import subprocess, os, sys
file = open("filename", "w")
try:
    proc = subprocess.Popen("nosuchprogram", stdout=file)
except OSError:
    file.close()
    sys.exc_clear() # here we go....
    os.remove("filename") # now we can delete file!