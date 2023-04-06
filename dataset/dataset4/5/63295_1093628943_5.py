import multiprocessing.pool
import time
class Pool(multiprocessing.pool.Pool):
    def _maintain_pool(self):
        time.sleep(2)
        super(Pool, self)._maintain_pool()
    def _repopulate_pool(self):
        assert self._state == multiprocessing.pool.RUN
        super(Pool, self)._repopulate_pool()
    @staticmethod
    def _handle_tasks(taskqueue, put, outqueue, pool):
        time.sleep(1)
        _real_handle_tasks(taskqueue, put, outqueue, pool)
_real_handle_tasks = multiprocessing.pool.Pool._handle_tasks
multiprocessing.pool.Pool._handle_tasks = Pool._handle_tasks
pool = Pool(4)
pool.map(str, range(10))
pool.map_async(str, range(10))
pool.terminate()
pool.join()