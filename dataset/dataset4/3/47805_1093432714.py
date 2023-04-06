class rec:
    def __str__(self):
        return str(self)

def overflower(x):
    try:
        return overflower(x)
    except:
        print (x)

list_rec = [100000000001]
for _ in range(12): list_rec = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[list_rec]]]]]]]]]]]]]]]]]]]]]]]]]
]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

str_rec = rec()

overflower(1) # OK
overflower(list_rec) # Aborts
overflower(str_rec) # Aborts