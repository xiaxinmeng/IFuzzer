def __del__(self):
    def actual_cleanup_code():
        ...
    def thread_dispatcher():
        loop.call_soon_threadsafe(actual_cleanup_code)
    thread = threading.Thread(target=thread_dispatcher)
    thread.start()