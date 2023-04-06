from pickletools import dis
import pickle
t = 1,
s1 = pickle.dumps(t, 0)
s2 = pickle.dumps(pickle.loads(s1), 0)
print(s1 == s2)
dis(s1)
dis(s2)