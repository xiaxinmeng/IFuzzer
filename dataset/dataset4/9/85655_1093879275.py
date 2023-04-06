import io
import logging.handlers
import threading
import time

class SlowHandler:
    def __init__(self):
        self.stream = io.StringIO()
        self.streamHandler = logging.StreamHandler(self.stream)

    def handle(self, msg):
        time.sleep(1)
        self.streamHandler.handle(msg)

target = SlowHandler()
mem_hdlr = logging.handlers.MemoryHandler(10, logging.ERROR, target)
mem_logger = logging.getLogger('mem')
mem_logger.propagate = False
mem_logger.addHandler(mem_hdlr)

def toggleTarget():
    time.sleep(1)
    mem_hdlr.setTarget(None)

t = threading.Thread(target=toggleTarget, args=())
t.daemon = True
t.start()

while True:
    time.sleep(0.1)
    mem_logger.warning("warning not flushed")
    mem_logger.error("error is flushed")
    print("%s" % target.stream.getvalue().splitlines())