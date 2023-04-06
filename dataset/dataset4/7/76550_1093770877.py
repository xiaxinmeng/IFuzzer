self.assertFalse(remaining_fds & fds_to_keep & open_fds,
                 "Some fds not in pass_fds were left open")