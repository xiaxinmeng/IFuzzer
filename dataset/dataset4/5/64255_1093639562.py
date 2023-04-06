with self.assertWarns(DeprecationWarning) if windows else contextlib.ExitStack():
    shutil.rmtree(victim)