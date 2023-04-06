def func(l):
    def get(i):
        return l[i]


    print(sum(get(i) for i in range(len(l)))) # works as expected, prints 10
    print(eval("get(0) + get(1) + get(2) + get(3)")) # works just fine, prints 10

    # if __globals is set to locals(), it still works, prints 10
    print(eval("sum(get(i) for i in range(len(l)))", locals()))

    # This will complain
    print(eval("sum(get(i) for i in range(len(l)))"))

func([1,2,3,4])