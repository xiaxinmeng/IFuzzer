# If you run the code below on Py30a3 you get the output shown at the end
import calendar, datetime, time

pastdate = datetime.datetime(1969, 12, 31)
print(pastdate)
timestamp = calendar.timegm(pastdate.utctimetuple())
print(timestamp)
try:
    pastdate_x = datetime.datetime.utcfromtimestamp(timestamp)
except ValueError as err:
    print("FAIL", err)
try:
    print(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(timestamp)))
except ValueError as err:
    print("FAIL", err)