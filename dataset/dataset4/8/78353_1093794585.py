import multiprocessing

def the_test():
    print("Begin")
    for x in multiprocessing.Pool().imap(int,
            ["4", "3"]):
        print(x)
    print("End")

the_test()