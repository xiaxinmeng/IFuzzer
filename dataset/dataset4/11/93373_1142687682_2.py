def total_microseconds(td: datetime.timedelta) -> int:
    return int(td.total_seconds() * 10**6)