def open_lines(name, mode='rt', buffering=-1):
    with open(name, mode, buffering) as f:
        for line in f:
            yield line

def logged_lines(f):
    try:
        for line in f:
            logging.warning(line.strip())
            yield line
    finally:
        f.close()

lines = open_lines('yyy', 'r')
if verbose:
    lines = logged_lines(lines)
try:
    for line in lines:
        print(line)
finally:
    lines.close()