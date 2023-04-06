def test_debug_mode_interop(self):
        # https://bugs.python.org/issue32636
        code = textwrap.dedent("""
            import asyncio

            async def native_coro():
                pass

            @asyncio.coroutine
            def old_style_coro():
                yield from native_coro()

            asyncio.run(old_style_coro())
        """)
        assert_python_ok("-c", code, PYTHONASYNCIODEBUG="1")