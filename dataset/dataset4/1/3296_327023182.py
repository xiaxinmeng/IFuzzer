
        # XXX: Posix compiant asctime should refuse to convert
        # year > 9999, but Linux implementation does not.
        # self.assertRaises(ValueError, time.asctime,
        #                  (12345, 1, 0, 0, 0, 0, 0, 0, 0))
        # XXX: For now, just make sure we don't have a crash:
