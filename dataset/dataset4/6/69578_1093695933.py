import difflib

first = u'location,location,location'
for second in (
    u'location.location.location',  # two periods (no commas)
    u'location.location,location',  # period after first
    u'location,location.location',  # period after second
    u'location,location,location',  # perfect match
):
    edit_dist = difflib.SequenceMatcher(None, first, second).ratio()
    print("comparing %r vs. %r gives edit dist: %g" % (first, second, edit_dist))