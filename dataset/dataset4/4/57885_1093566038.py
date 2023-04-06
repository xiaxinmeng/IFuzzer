import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()