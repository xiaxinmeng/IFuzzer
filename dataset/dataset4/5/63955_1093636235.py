class NetworkedNNTP_SSLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        with support.transient_internet(cls.NNTP_HOST):
            cls.server = NNTP_SSL(cls.NNTP_HOST, timeout=TIMEOUT)
    
    def test_that_triggered_the_failure(self):
        with support.transient_internet(self.NNTP_HOST):
            ...  # Suppose this timed out and the test was skipped
    
    def test_capabilities(self):
        # Now this is reusing the existing connection, left in a broken state by
        # the previous test
        self.server.capabilities()