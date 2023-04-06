import socket, time, sys

PORT = 9999
DEST_ADDR = ("192.168.1.60", PORT)

def run():
    maxcount = 100
    data = "pingme pingme pingme pingme pingme..."
    dest = DEST_ADDR