class MyDate(datetime):

    @classmethod
    def fromDT(cls, d):
        """ :type d: datetime """
        return cls(d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, d.tzinfo)

    def replace(self, *args, **kw):
        """ :type other: datetime.timedelta
            :rtype: MyDate """
        return self.fromDT(super(MyDate, self).replace(*args, **kw))