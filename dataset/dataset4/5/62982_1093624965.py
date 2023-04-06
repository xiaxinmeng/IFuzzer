import multiprocessing
import platform
import sqlite3
import sys

print(sys.version)
print(sqlite3.version)
print(sqlite3.sqlite_version)
print(multiprocessing.__version__)
print(multiprocessing.cpu_count())
print(platform.platform())