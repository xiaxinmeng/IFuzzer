
class Blerg():
    def __init__(self):
        self.q = multiprocessing.Queue(-1)

    def print_queue(self):
        print("Queue", self.q)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')

    blerg = Blerg()

    blerg.print_queue()

    proc = multiprocessing.Process(target=blerg.print_queue)
    proc.start()
