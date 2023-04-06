import xmlrpc.client; from xmlrpc.client import escape
text = "...\u043c......<"
print(escape(text))