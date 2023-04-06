class ExtendedEncoder(json.JSONEncoder):
    """An extended JSON encoder which knows about other data types."""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, timedelta):
            # as_timedelta() does not recognize microseconds, so convert these
            # to floating seconds, but only if there are any seconds.
            if obj.seconds > 0 or obj.microseconds > 0:
                seconds = obj.seconds + obj.microseconds / 1000000.0
                return '{0}d{1}s'.format(obj.days, seconds)
            return '{0}d'.format(obj.days)
        elif isinstance(obj, Enum):
            # It's up to the decoding validator to associate this name with
            # the right Enum class.
            return obj.name
        return json.JSONEncoder.default(self, obj)