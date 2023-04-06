hits= []
for i in range(100):
    hits.append(random.choices(["A","B","C","D"], [0, 0, 0, 0])[0])
print (set(hits))