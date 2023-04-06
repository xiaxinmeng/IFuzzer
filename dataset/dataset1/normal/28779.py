import multiprocessing
import os

def f():
    pass

multiprocessing.Lock()

if __name__ == "__main__":
    ctx = multiprocessing.get_context('forkserver')
    # modname is the script's importable name (not "__main__")
    modname = os.path.basename(__file__).split(".")[0]
    ctx.set_forkserver_preload([modname])
    proc = ctx.Process(target=f)
    proc.start()
    proc.join()
