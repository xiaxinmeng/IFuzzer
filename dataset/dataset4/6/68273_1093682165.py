import os, re, resource
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

with open("/proc/%d/status" % os.getpid(), "r") as f:
    for line in f:
        if line.split(':')[0] in ('VmHWM', 'VmRSS'):
            print(line.strip())