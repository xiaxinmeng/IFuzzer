def fxn():
    # user warnings are not ignored by default and will cause a dump of information
    # to standard error.
    warnings.warn("User warning: Warn on purpose for IDLE", UserWarning)

if __name__ == "__main__":
    fxn()
    print("the program should not terminate with the warning, but keep on running")
    a = 10 * 1000
    print(a)

    # exception testing each of these will stop the program
    # divide by zero
    b = 10 * (1/0)
    print(b)
    # variable not defined
    c = 4 + spam*3
    print(c)
    # can't convert 'int' object o str implicitly
    d = '2' + 2
    print(d)