# Case 2) The day to rollover is further in the interval (i.e., today is
#         day 2 (Wednesday) and rollover is on day 6 (Sunday).  Days to
#         next rollover is simply 6 - 2 - 1, or 3.
# Case 3) The day to rollover is behind us in the interval (i.e., today
#         is day 5 (Saturday) and rollover is on day 3 (Thursday).
#         Days to rollover is 6 - 5 + 3, or 4.  In this case, it's the
#         number of days left in the current week (1) plus the number
#         of days in the next week until the rollover day (3).
if when.startswith('W'):
   day = t[6] # 0 is Monday
   if day > self.dayOfWeek:
       daysToWait = (day - self.dayOfWeek) - 1
       self.rolloverAt = self.rolloverAt + (daysToWait * (60 * 60 * 24))
   if day < self.dayOfWeek:
       daysToWait = (6 - self.dayOfWeek) + day