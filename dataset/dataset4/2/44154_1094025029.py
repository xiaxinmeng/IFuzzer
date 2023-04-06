import ctypes
ctypes.CDLL('/System/Library/Frameworks/CoreData.framework/CoreData')
import sqlite3
sqlite3.connect(":memory:")