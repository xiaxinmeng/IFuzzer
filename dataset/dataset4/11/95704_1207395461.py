async def test_cancellation_in_body_child_propagation(self):
        """
        If the task running the TaskGroup is blocked on something and then
        cancelled, the TG children are cancelled too.

        If the children raise an exception different than `CancelledError`
        while being stopped, those exceptions are raised in an ExceptionGroup.
        """
        LONG_SLEEP = 10  # The awaiter is expected to be cancelled waiting on this.

        exc = RuntimeError()

        async def foo():
            try:
                await asyncio.sleep(LONG_SLEEP)
            except CancelledError:
                # We raise, and expect it to be propagated.
                raise exc  # Something other than a CancelledError.

        async def runner():
            async with taskgroups.TaskGroup() as g:
                g.create_task(foo())

                await asyncio.sleep(LONG_SLEEP)

        r = asyncio.create_task(runner())
        await asyncio.sleep(0.1)

        self.assertFalse(r.done())
        r.cancel()
        with self.assertRaises(ExceptionGroup) as cm:
            await r

        self.assertEqual(cm.exception == ExceptionGroup([exc]))