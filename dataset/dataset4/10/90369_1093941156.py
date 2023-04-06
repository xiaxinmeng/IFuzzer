import socket
from test.test_ftplib import TestFTPClass,TIMEOUT

def test_makepasv():
    host, port = TestFTPClass.client.makepasv()
    conn = socket.create_connection((test_makepasv(), host), timeout=TIMEOUT)
    conn.close()