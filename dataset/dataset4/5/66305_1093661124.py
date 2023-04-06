os.mkdir('dir')
os.access('dir', os.W_OK)          # what returns?
os.access('nonexistent', os.W_OK)  # what returns or raises?