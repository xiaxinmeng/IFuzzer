class ReactorShutdownInteraction(unittest.TestCase):
    """Test reactor shutdown interaction"""

    def setUp(self):
        """Start a UDP port"""
        self.server = Server()
        self.port = reactor.listenUDP(0, self.server, interface='127.0.0.1')

    def tearDown(self):
        """Stop the UDP port"""
        return self.port.stopListening()