
class ComparisonError(Exception):
    pass

class Incomparable:
    def __eq__(self, other):
        raise ComparisonError

key = Incomparable()
with self.assertRaises(ComparisonError):
    zoneinfo.ZoneInfo(key)
