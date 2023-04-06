# This very quickly and consistently hangs after a few attempts on my machines
def run(x):
    print("Worker with ", x)
    return x

def main():
    for i in range(1000):
        print("Attempt #", i)
        from multiprocessing import Pool

        with Pool(processes=16, maxtasksperchild=1) as p:
            for entry in p.imap_unordered(run, range(50)):
                print("Main received back ", entry)


if __name__ == "__main__":
    main()