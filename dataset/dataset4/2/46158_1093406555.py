if when.startswith('W'):
    day = t[6] # 0 is Monday
    if day != self.dayOfWeek:
        if day < self.dayOfWeek:
            daysToWait = self.dayOfWeek - day - 1
        else:
            daysToWait = 6 - day + self.dayOfWeek
        self.rolloverAt = self.rolloverAt + (daysToWait * (60 * 60 * 24))