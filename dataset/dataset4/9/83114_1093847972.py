x=[2,3]
[f(x) for f in [(lambda a:a[i]) for i in [0,1]]]
#the expected output is [2,3] but actual is [3,3]
[f(x) for f in [lambda a:a[0],lambda a:a[1]]]
#results [2,3] normally