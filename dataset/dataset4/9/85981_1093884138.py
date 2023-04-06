
import sqlite3
target = sqlite3.connect(':memory:')
source = sqlite3.connect(':memory:')
source.close()
source.backup(target)
