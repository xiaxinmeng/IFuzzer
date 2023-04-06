import codecs
def pace_by_one(exc):
    return ('\ufffd', exc.start+1)

codecs.register_error('pace_by_one', pace_by_one)
