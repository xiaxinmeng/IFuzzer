expected = [self._call_matcher(c) for c in calls]
cause = expected if isinstance(expected, Exception) else None