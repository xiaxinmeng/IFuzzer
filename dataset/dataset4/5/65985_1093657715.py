if result != expected_text:
   print_diffs(expected_text, result)
   self.fail("outputs are not equal, see diff above")