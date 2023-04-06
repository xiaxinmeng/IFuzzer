import threading
import time

th = threading.Thread(target=lambda: time.sleep(5.0))
th.start()
th.join('blah')
th.join  # Used to hang