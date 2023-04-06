def test_no_name_argument(self):
  if self.mode.endswith("bz2") or self.mode.endswith("xz"):
    # BZ2File and LZMAFile have no name attribute.
    return