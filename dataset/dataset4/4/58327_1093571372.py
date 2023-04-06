self._call_queue = multiprocessing.Queue(self._max_workers +
                                                 EXTRA_QUEUED_CALLS)