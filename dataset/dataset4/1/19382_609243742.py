class SubinterpThreadingTests(unittest.TestCase):
    def test_lzma_subinterp(self):
        code = textwrap.dedent(r"""
            import os
            from lzma import LZMACompressor, LZMADecompressor, LZMAError
            lzc = LZMACompressor()
            lzd = LZMADecompressor()
            def noop(*args):
                pass

            os.register_at_fork(after_in_child=noop)
        """)
        ret = support.run_in_subinterp(code)