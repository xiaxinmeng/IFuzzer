class Timestamp(datetime.datetime):

    def __new__(cls, raw_value, *args, **kwargs):
        if not args and not kwargs:
            return cls.fromtimestamp(int(raw_value))
        else:
            return super(Timestamp, cls).__new__(cls, raw_value,
                                                 *args, **kwargs)

    def __str__(self):
        return str(int(time.mktime(self.timetuple())))