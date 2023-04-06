# Issue python/cpython#54485 - check that inputs >=4GB are handled correctly.
class ChecksumBigBufferTestCase(unittest.TestCase):

    def setUp(self):
        with open(support.TESTFN, "wb+") as f:
            f.seek(_4G)
            f.write(b"asdf")
        with open(support.TESTFN, "rb") as f:
            self.mapping = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    def tearDown(self):
        self.mapping.close()
        support.unlink(support.TESTFN)