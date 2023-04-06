import re
a = """0xd26935a5ee4cd542e8a3a7e74fb7a99855975b59\n"""

eth_re = re.compile(r'^0x[0-9a-fA-F]{40}$')

print(eth_re.match(a))
print(len(a)) # 长度43