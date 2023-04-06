
with open("data.bin", "rb") as f:
    data = f.read()

base = 15403807 * b'\xff'
longer = base + b'\xff'

print(data.find(base))
print(data.find(longer))
