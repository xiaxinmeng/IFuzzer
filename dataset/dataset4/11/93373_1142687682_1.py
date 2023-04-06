def total_microseconds(td: datetime.timedelta) -> int:
    return (td.days * 86400 + td.seconds) * 10**6 + td.microseconds