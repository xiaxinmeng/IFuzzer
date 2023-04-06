new = old.astimezone(tz)  # no conversion if old was naive
new = old.replace(tzinfo=tz) # no conversion ever