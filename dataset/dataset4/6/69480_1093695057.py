class MyThread(Thread):
    def run(self):
        initialize()
        try: super().run()
        finally: finalize()

with ThreadPoolExecutor(thread_class=MyThread): ...