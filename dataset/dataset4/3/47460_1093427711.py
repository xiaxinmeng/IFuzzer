import subprocess, os

file = open("filename", "w")
try:
    proc = subprocess.Popen("nosuchprogram", stdout=file)
except OSError:
    pass