import unittest

import datetime as datetime_module
from datetime import timedelta
from datetime import tzinfo
from datetime import time
from datetime import timezone
from datetime import date, datetime
import time as _time

import _strptime

class SubclassDatetime(datetime):
    sub_var = 1

class TestDateTime(unittest.TestCase):
    theclass = datetime

    def test_more_strftime(self):
        # This tests fields beyond those tested by the TestDate.test_strftime.
        t = self.theclass(2004, 12, 31, 6, 22, 33, 47)
        self.assertEqual(t.strftime("%m %d %y %f %S %M %H %j"),
                                    "12 31 04 000047 33 22 06 366")
        for (s, us), z in [((33, 123), "33.000123"), ((33, 0), "33"),]:
            tz = timezone(-timedelta(hours=2, seconds=s, microseconds=us))
            t = t.replace(tzinfo=tz)
            self.assertEqual(t.strftime("%z"), "-0200" + z)

        # bpo-34482: Check that surrogates don't cause a crash.
        try:
            t.strftime('%y\ud800%m %H\ud800%M')
        except UnicodeEncodeError:
            pass

class TestDateTimeTZ(TestDateTime, unittest.TestCase):
    theclass = datetime

class TestSubclassDateTime(TestDateTime):
    theclass = SubclassDatetime
    def test_roundtrip(self):
        pass
