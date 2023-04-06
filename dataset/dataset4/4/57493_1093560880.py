def formatdatetime(dt_object):
    return email.utils.formatdate(time.mktime(dt_object.utctimetuple()) + 1e-6 * a.microsecond - time.timezone)