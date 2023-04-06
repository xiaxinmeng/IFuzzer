import sqlite3
import multiprocessing as mp

def main():
    ## --- create a database
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()