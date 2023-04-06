
async def shutdown_default_executor(self):
    fut = self.create_future()
    th = threading.Thread(func=self._do_shutdown, args=(fut,))
    th.start()
    await fut
    th.join()

def _do_shutdown(self, fut):
   try:
       self._executor.shutdown(wait=True)
       self.call_soon_threadsafe(fut.set_result, None)
   except Exception as ex:
       self.call_soon_threadsafe(fut.set_exception, ex) 
