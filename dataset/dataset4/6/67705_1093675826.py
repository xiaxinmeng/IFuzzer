from datetime import datetime
t = datetime.utcnow().timestamp()
t2 = datetime.utcfromtimestamp(t)
assert t == t2, 'Moving from timestamp and back should always work'