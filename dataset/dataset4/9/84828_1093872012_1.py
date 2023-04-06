os.chmod(TESTFN, 0o700)
st_mode, modestr = self.get_mode()
self.assertEqual(modestr[:3], '-rw')
self.assertS_IS("REG", st_mode)
self.assertEqual(self.statmod.S_IFMT(st_mode),
                 self.statmod.S_IFREG)