nntp = NNTP("localhost")
abort = False
try:
    ...
    try:
        nntp.body("<example>", file="/dev/full")
    except (NNTPTemporaryError, NNTPPermanentError):
        raise  # NNTP connection still intact
    except:
        abort = True
        raise
    ...
finally:
    try:
        nntp.quit()
    except NNTPError:
        # Connection cleaned up despite exception
        if not abort:
            raise