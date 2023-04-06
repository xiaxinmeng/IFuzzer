def new_rfcformat(self, default_utcoffset='-00:00'):
    if we_know_the_utc_offset:
        return self.rfcformat() # the method in my current patch
    else:
        return self.isoformat() + default_utcoffset