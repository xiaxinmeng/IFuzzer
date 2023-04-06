class PosixPollSerial(Serial):
    """\
    Poll based read implementation. Not all systems support poll properly.
    However this one has better handling of errors, such as a device
    disconnecting while it's in use (e.g. USB-serial unplugged).
    """