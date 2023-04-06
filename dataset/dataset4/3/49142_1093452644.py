import sys
from multiprocessing import Process,Pipe, reduction

def main():
    print("starting");
    i, o = Pipe(False)
    parent, child = Pipe();
    reducedchild = reduce_pipe(child);
    p = Process(target=helper, args=(i,));
    p.start();
    parent.send("hi");
    o.send(reducedchild);
    print(parent.recv());
    print("finishing");
    p.join();
    print("done");

def helper(inPipe):
    childPipe = expand_reduced_pipe(inPipe.recv());
    childPipe.send("child got: " + childPipe.recv());
    return;

def reduce_pipe(pipe):
    if sys.platform == "win32":
        return reduction.reduce_pipe_connection(pipe);
    else:
        return reduction.reduce_connection(pipe);

def expand_reduced_pipe(reduced_pipe):
    return reduced_pipe[0](*reduced_pipe[1]);

if __name__ == "__main__":
    main();