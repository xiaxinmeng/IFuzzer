with open("mydata.txt") as fp:
    for line in iter(fp.readline, "STOP"):
        process_line(line)