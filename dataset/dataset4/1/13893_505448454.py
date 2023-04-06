
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self._threads_lock = threading.Lock()
    self._threads = []
