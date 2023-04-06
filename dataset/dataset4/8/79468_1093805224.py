from difflib import SequenceMatcher
seqMatcher = SequenceMatcher(None, "德阳孩子", "孩子德阳")
seqMatcher.get_matching_blocks()