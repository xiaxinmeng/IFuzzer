def rootOnly(f):
        """Decorator to skip tests that require root access"""
        def wrapper(self):
                self.skipIf(os.getuid() != 0, "Must be root")
                self.f()
        wrapper.__doc__ = f.__doc__
        return wrapper


class ReadShadowTest(unittest.TestCase):
        """Read access to /etc/shadow"""
        @rootOnly
        def testReadingAsRoot(self):
                """Reading /etc/shadow as root"""
                open("/etc/shadow").close()