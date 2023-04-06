
class MyThread(threading.Thread):
    def run(self):
        with some_important_context():
            super().run()
