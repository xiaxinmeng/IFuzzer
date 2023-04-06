#import warnings
import tracemalloc
tracemalloc.start(10)
f = open("/etc/issue")
f = None