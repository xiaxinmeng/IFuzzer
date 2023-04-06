data = msg.as_bytes()

msg2 = message_from_bytes(data)
print(x)
print(msg2[header])
assert msg2[header] == x