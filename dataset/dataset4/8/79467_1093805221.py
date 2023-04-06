from difflib import SequenceMatcher
seqMatcher = SequenceMatcher(None, u"德阳孩子", u"孩子德阳")
seqMatcher.get_matching_blocks()