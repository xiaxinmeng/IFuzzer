instance = foo()
print(await instance)  # Okay the first time
print(await instance)  # Second time should be an error