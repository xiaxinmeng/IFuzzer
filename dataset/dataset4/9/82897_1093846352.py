class MyHandler(BaseRotatingHandler):
    def __init__(self, *args, **kwargs):
        super(MyHandler, self).__init__(*args, **kwargs)
        self.namer = self.my_namer
        self.rotator = self.my_rotator

    def my_namer(self, default_name):
        return default_name  # or whatever you want here

    def my_rotator(self, source, dest):
        os.rename(source, dest)  # or whatever you want here