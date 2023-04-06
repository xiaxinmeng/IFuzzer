def logged_lines(f):
    try:
        for line in f:
            logging.warning(line.strip())
            yield line
    finally:
        logging.warning('closing')


f = open('yyy', 'r')
try:
    for l in logged_lines(f):
       print(l)
finally:
    f.close()