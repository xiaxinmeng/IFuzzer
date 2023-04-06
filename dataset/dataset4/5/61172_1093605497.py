class ThreadPoolMixin(ExecutorMixin):
    executor_type = futures.ThreadPoolExecutor

    def run(self, result):
        key = test.support.threading_setup()
        try:
            return super().run(result)
        finally:
            test.support.threading_cleanup(*key)


class ProcessPoolMixin(ExecutorMixin):
    executor_type = futures.ProcessPoolExecutor

    def run(self, result):
        try:
            return super().run(result)
        finally:
            test.support.reap_children()