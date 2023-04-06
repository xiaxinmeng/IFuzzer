def test_compile_all_2038(self):
    with open(self.source_path, 'r') as f:
        os.utime(f.name, (2147558400, 2147558400)) # Jan 20, 2038 as touch
    self.assertTrue(compileall.compile_file(pathlib.Path(self.source_path)))