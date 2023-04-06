def sigint_handler():
    get_running_loop().interrupt()

# in class BaseEventLoop
def interrupt(self):
    # Might be a generally useful thread-safe way to interrupt a loop
    if self._is_inside_callback():
        _thread.interrupt_main() # All this behavior is only relevant to the main thread anyway
    else:
        self._interrupted = True