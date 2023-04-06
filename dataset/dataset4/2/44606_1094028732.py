if lt.tm_zone is None:
  self.assert_(not hasattr(time, "tzname"))
else:
  self.assertEqual(lt.tm_zone, time.tzname[lt.tm_isdst])