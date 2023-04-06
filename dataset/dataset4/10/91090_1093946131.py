
import multiprocessing
import time


class Application:

    def __init__(self):
        self._event = multiprocessing.Event()
        self._processes = [
            multiprocessing.Process(target=self._worker)
            for _ in range(multiprocessing.cpu_count())]

    def _worker(self):
        while not self._event.is_set():
            print(multiprocessing.current_process().name)
            time.sleep(1)

    def start(self):
        for process in self._processes:
            print('starting')
            process.start()

    def stop(self):
        self._event.set()
        for process in self._processes:
            process.join()


if __name__ == '__main__':
    application = Application()
    application.start()
    time.sleep(3)
    application.stop()
