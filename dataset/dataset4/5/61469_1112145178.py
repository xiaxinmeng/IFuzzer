def convert_time_to_utc(time_of_day):
    return ( time_of_day - time_of_day.utcoffset() ).replace(tzinfo=timezone.utc)