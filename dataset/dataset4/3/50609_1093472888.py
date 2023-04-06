#!/usr/bin/python3.2
# xmlclient.py
import xmlrpc.client
server_proxy = xmlrpc.client.ServerProxy("http://localhost:8000")
print(server_proxy.print_str("Bonjour"))
print(server_proxy.print_str("Je suis à Montréal"))