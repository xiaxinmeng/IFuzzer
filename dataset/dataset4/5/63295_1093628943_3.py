import multiprocessing.pool
import time
class ThreadPool(multiprocessing.pool.ThreadPool):
    def _maintain_pool(self):
        time.sleep(1)
        super(ThreadPool, self)._maintain_pool()
    def _repopulate_pool(self):
        assert self._state == multiprocessing.pool.RUN
        super(ThreadPool, self)._repopulate_pool()
pool = ThreadPool(4)
pool.map(lambda x: x, range(5))
pool.terminate()
pool.join()