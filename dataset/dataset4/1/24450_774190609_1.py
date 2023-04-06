class Stringy(str):
    def __new__(cls, value):
        rv = super().__new__(cls, value)
        rv.allow_comparisons = True
    def __eq__(self, other):
        if not self.allow_comparisons:
            raise ComparisonError
        return super().__eq__(other)
    def __hash__(self):
        return hash(self[:])

key = Stringy("America/New_York")
zoneinfo.ZoneInfo(key)
key.allow_comparisons = False
try:
    # Note: This is try/except rather than assertRaises because there is no guarantee
    # that the key is even still in the cache, or that the key for the cache is the original
    # `key` object.
    zoneinfo.ZoneInfo.clear_cache(only_keys="America/New_York")
except ComparisonError:
    pass