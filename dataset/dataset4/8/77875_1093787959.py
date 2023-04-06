class _ProactorReadPipeTransport(_ProactorBasePipeTransport,
                                 transports.ReadTransport):
    """Transport for read pipes."""
    (...)
    def pause_reading(self):
        if self._closing or self._paused:
            return
        self._paused = True

        if self._read_fut is not None and not self._read_fut.done():
            # TODO: This is an ugly hack to cancel the current read future
            # *and* avoid potential race conditions, as read cancellation
            # goes through `future.cancel()` and `loop.call_soon()`.
            # We then use this special attribute in the reader callback to
            # exit *immediately* without doing any cleanup/rescheduling.
            self._read_fut.__asyncio_cancelled_on_pause__ = True

            self._read_fut.cancel()
            self._read_fut = None
            self._reschedule_on_resume = True

        if self._loop.get_debug():
            logger.debug("%r pauses reading", self)