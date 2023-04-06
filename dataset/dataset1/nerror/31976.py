import threading
import io
import time
import _pyio

class MyFileIO(io.FileIO):
    def flush(self):
        # Simulate a slow flush. Slow disk, etc.
        time.sleep(0.25)
        super().flush()

raw = MyFileIO('test.dat', 'wb')
#fp = _pyio.BufferedWriter(raw)
fp = io.BufferedWriter(raw)
t1 = threading.Thread(target=fp.close)
t1.start()
time.sleep(0.1) # Ensure t1 is sleeping in fp.close()/raw.flush()
fp.write(b'test')
t1.join()
