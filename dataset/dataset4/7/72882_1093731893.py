@staticmethod
def _handle_workers(pool):
    thread = threading.current_thread()

    # Keep maintaining workers until the cache gets drained, unless the pool
    # is terminated.
    while thread._state == RUN or (pool._cache and thread._state != TERMINATE):
        pool._maintain_pool()
        time.sleep(0.1)
    # send sentinel to stop workers
    pool._taskqueue.put(None)
    util.debug('worker handler exiting')