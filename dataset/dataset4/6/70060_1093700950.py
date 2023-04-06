import threading
import traceback

def main():
    with open(__file__, 'a') as fp:
        fp.write(' ')
        traceback.format_stack()

threads = [
    threading.Thread(target=main)
    for i in range(100)
]
map(lambda t: t.start(), threads)
map(lambda t: t.join(), threads)