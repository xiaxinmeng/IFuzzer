import datetime

def rfcformat(dt):
    """ Output datetime in RFC 3339 format that is also valid ISO 8601
        timestamp representation"""

    if dt.tzinfo is None:
        suffix = "-00:00"
    else:
        suffix = dt.strftime("%z")
        suffix = suffix[:-2] + ":" + suffix[-2:]
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + suffix