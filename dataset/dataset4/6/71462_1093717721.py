d = ExpiringDict(max_len=3, max_age_seconds=0.01)
d['a'] = 'z'
sleep(1)
d.popitem()