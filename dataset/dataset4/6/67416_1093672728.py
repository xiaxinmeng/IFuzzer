def logged_lines(f):
    try:
        for line in f:
            logging.warning(line.strip())
            yield line
    finally:
        logging.warning('closing')
        f.close()