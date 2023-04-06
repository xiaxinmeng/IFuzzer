from datetime import datetime
a_datetime = datetime.now()
a_datetime = a_datetime.replace(microsecond = 1)

iso_str = a_datetime.isoformat()
b_datetime = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%f")

assert(a_datetime == b_datetime)