class ReactorShutdownInteraction(unittest.TestCase):
    """Test reactor shutdown interaction"""

    def setUp(self):
        """Start a UDP port"""
        self.server = Server()
        self.port = reactor.listenUDP(0, self.server, interface='127.0.0.1')
        # Stop the UDP port after the test completes.
        self.addCleanup(self.port.stopListening)