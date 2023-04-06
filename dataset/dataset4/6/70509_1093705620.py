##
##  It appears that strptime is ignoring the AM/PM field
##
from datetime import datetime
d1 = datetime.strptime("1:00 PM", "%H:%M %p")
d2 = datetime.strptime("1:00 AM", "%H:%M %p")
d1.hour, d2.hour
(1, 1) # d1 should be 13
d1 == d2
True # and these should not be equal