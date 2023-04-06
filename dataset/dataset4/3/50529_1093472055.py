EPOCH = 1970
_EPOCH_DATETIME = datetime.datetime(EPOCH, 1, 1)
_SECOND = datetime.timedelta(seconds=1)

def timegm(tuple):
    """Unrelated but handy function to calculate Unix timestamp from GMT."""
    return (datetime.datetime(*tuple[:6]) - _EPOCH_DATETIME) // _SECOND