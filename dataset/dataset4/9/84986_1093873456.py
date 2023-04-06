a = [1,1,1,1]

for i in a:
    if a.count(i) > 1:
        a.remove(i)
 
print(a)