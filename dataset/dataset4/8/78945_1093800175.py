with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)