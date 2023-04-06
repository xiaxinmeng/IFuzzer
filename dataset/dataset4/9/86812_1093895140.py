def apply(obj, function, /, args=(), kwargs={}):
    try:
        new = obj.copy()
    except AttributeError:
        from copy import copy
        new = copy(obj)
    function(new, *args, **kwargs)
    return new
# implement reversed() for list
lis = [1, 2, 3, 4, 5]
arr = apply(lis, list.reverse)
print(arr)  # [5, 4, 3, 2, 1]