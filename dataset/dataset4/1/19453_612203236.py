
while (len(self._processes) < len(self._pending_work_items)
            and len(self._processes) < self._max_workers):
    p = self._mp_context.Process(
               target=_process_worker,
               args=(self._call_queue,
                           self._result_queue,
                           self._initializer,
                           self._initargs))
    p.start()
    self._processes[p.pid] = p
