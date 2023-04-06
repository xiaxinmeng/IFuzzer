from multiprocessing import Pool

def main():
    p = Pool();
    blah = [];
    print("Mapping");
    p.map(dummy, blah);
    p.close();
    p.join(); # deadlocks here
    print("Done");

def dummy(x):
    pass;

if __name__ == "__main__":
    main();