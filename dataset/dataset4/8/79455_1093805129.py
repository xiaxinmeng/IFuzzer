import time
print("\x98")
with open("x", "w") as fp:
    fp.write("done\n")
    fp.flush()
print("wait")
time.sleep(5)
print("exit")