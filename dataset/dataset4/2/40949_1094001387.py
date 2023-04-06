class ReadShadowTest(unittest.TestCase):
        """Read access to /etc/shadow"""
        def testReadingAsRoot(self):
                """Reading /etc/shadow as root"""
                self.skipIf(os.geteuid() != 0, "Must be root")
                open("/etc/shadow").close()