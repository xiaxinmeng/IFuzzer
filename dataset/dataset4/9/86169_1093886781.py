c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print("1:",c) # right: {'one': 1, 'two': 2, 'three': 3}

b= zip(['one', 'two', 'three'], [1, 2, 3])
a= list(b) #Because of this line of code, the result is different
print("2:",dict(b)) #wrong: {}

b= zip(['one', 'two', 'three'], [1, 2, 3])
a= tuple(b) #Because of this line of code, the result is different
print("2:",dict(b)) #wrong: {}