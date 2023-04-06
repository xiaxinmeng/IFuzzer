import sys, getpass
from telnetlib import Telnet

HOST = "localhost"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

def filter_cb(session, data):
    sys.stdout.write(data)
    return data

tn = Telnet(HOST)
tn.set_data_filter_callback(filter_cb)
tn.read_until("login: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")
tn.read_until("logout")