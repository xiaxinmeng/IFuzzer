import atexit
from multiprocessing import util
from multiprocessing import get_context

util.log_to_stderr(5)

executor = None

@atexit.register
def run_last():
    global executor
    if executor:
        f = executor.submit(id, None)
        util.debug("running future on executor flag {}\n\n\n".format(
            executor._shutdown_thread))
        f.result()


from concurrent.futures import ProcessPoolExecutor
if __name__ == "__main__":
    context = get_context('spawn')
    executor = ProcessPoolExecutor(5, mp_context=context)
    executor.submit(id, 42).result()