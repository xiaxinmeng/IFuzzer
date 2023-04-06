
class my_bytes(bytes):
  def dummy(self):
    print("dummy called")


x=my_bytes.fromhex("c0de c0de")
print(x.__class__)

print(x[1:].__class__)

