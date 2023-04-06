class X(int):
    def __del__(self):
        d.clear()
    
d = {i: X(i) for i in range(8)}
    
for result in d.items():
    if result[0] == 2:
        d[2] = None # free d[2] --> X(2).__del__ is called