import asyncio
import socket
import threading
import selectors
import time

class SelectThread(threading.Thread):
    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.selector = selectors.DefaultSelector()
        self.timeout = None
        self._quit = False

        # self-pipe to be able to stop immediately the thread
        # in stop()
        self.selfpipe_rfd, self.selfpipe_wfd = socket.socketpair()
        self.selector.register(self.selfpipe_rfd, selectors.EVENT_READ)

    def run(self):
        while not self._quit:
            events = self.selector.select(self.timeout)
            for event in events:
                self.loop.call_soon_threadsafe(print, "got event", event)

    def stop(self):
        self._quit = True
        # wake up selector
        self.selfpipe_wfd.send(b'x')
        self.join()

        self.selfpipe_rfd.close()
        self.selfpipe_wfd.close()
        self.selector.close()

loop = asyncio.get_event_loop()

rfd, wfd = socket.socketpair()

selector = SelectThread(loop)
selector.selector.register(rfd, selectors.EVENT_READ)
selector.start()

wfd.send(b'data')
selector.stop()

loop.run_until_complete(asyncio.sleep(1))

rfd.close()
wfd.close()
