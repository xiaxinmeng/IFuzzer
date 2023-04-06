import asyncore
import os

class FileDispatcher(asyncore.file_dispatcher):
    def handle_read(self):
        data = self.recv(8192)

fd = os.open('/etc/passwd', os.O_RDONLY)
s = FileDispatcher(fd)
os.close(fd)
asyncore.loop(timeout=0.01, use_poll=True, count=2)