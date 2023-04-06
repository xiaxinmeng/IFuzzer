with open("/dev/full", "wb") as file:
    file.write(b"data")
    print("All is well")
print("Not executed")