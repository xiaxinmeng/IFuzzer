class OtherTests(unittest.TestCase):
    ...

    def test_read_after_write_cp437_filenames(self):
        fname = 'test_cp437_é'
        with zipfile.ZipFile(TESTFN2, 'w') as zipfp:
            zipfp.writestr(fname, b'sample')

        with zipfile.ZipFile(TESTFN2) as zipfp:
            zinfo = zipfp.infolist()[0]
            # Ensure general purpose bit 11 (Language encoding flag
            # (EFS)) is unset to indicate the filename is not unicode
            self.assertFalse(zinfo.flag_bits & 0x800)
            self.assertEqual(zipfp.read(fname), b'sample')