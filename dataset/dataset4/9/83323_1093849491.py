class MyHandler(logging.StreamHandler):
    def __init__(self, resource, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resource: namedtuple = resource
    
    def emit(self, record):
        record.msg += f" {self.resource.type}"
        return super().emit(record)