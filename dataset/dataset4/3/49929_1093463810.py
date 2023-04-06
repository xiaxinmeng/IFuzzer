class TestSample(TestCase):

    def setUp(self):
        dirname = mkdtemp()
        self.addCleanup(shutils.rmtree, dirname, ignore_errors=True)
        db = make_db(dirname)
        self.addCleanup(db.tearDown)