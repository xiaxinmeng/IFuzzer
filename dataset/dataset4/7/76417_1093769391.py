with open("fifo", "wb", buffering=1) as out:
    for line in lines:
        out.write(line)