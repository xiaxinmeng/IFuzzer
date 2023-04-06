EPOCH = datetime(1970, 1, 1)
def timestamp(t):
      return (t - EPOCH).total_seconds()