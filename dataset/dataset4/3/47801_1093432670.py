from multiprocessing import *

latin = str

SENTINEL = latin('')

def _echo(conn):
    for msg in iter(conn.recv_bytes, SENTINEL):
        conn.send_bytes(msg)
    conn.close()