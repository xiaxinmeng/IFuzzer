def logged_lines(fname):
    f = open('yyy', 'r')
    try:
        for line in f:
            logging.warning(line.strip())
            yield line
    finally:
        logging.warning('closing')
        f.close()

for l in logged_lines('yyy'):
   print(l)