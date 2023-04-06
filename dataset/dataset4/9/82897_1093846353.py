class MyHandler(BaseRotatingHandler):
    def namer(self, default_name):
        return default_name  # or whatever you want here

    def rotator(self, source, dest):
        os.rename(source, dest)  # or whatever you want here