
def run_forever(self):
    assert self._self_reading_future is None
    try:
        super().run_forever()
    finally:
        if self._self_reading_future is not None:
            self._self_reading_future.cancel()
            self._self_reading_future = None
