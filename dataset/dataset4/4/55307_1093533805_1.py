import msvcrt
msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
msvcrt.setmode (1, os.O_BINARY) # stdout = 1
msvcrt.setmode (2, os.O_BINARY) # stderr = 2