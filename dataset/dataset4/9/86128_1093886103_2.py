class MyExecutor(ThreadPoolExecutor):
    def shutdown(self, *args, **kwargs):
        stop_my_tasks()
        super().shutdown(*args, **kwwargs)