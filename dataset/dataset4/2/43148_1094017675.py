os.dup2(2, 3) # backup fd 2

os.dup2(1, 2)
os.dup2(2, 1)

os.dup2(3, 2) # restore fd 2