def main():
    from multiprocessing import Pipe, reduction
    i, o = Pipe()
    print(i);
    reduced = reduction.reduce_connection(i)
    print(reduced);
    newi = reduced[0](*reduced[1])
    print(newi);
    newi.send("hi")
    o.recv()

if __name__ == "__main__":
    main();