import pickle, datetime
class mydate(datetime.date): pass
s = pickle.dumps(mydate.today())
broken = pickle.loads(s)
del broken
