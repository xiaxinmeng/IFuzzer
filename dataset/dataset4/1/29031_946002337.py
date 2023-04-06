
                # To prevent argparse from raising an exception about any
                # options in env_val that it mistakes for known option, we
                # strip out all double dashes and any dashes followed by a
                # character that is not for the option we are dealing with.
                #
                # Please note that order of the regex is important!  We must
                # strip out double-dashes first so that we don't end up with
                # substituting "--Long" to "-Long" and thus lead to "ong" being
                # used for a library directory.

