
from concurrent.futures import ProcessPoolExecutor


class ObjectWithPickleError():
    """Triggers a RuntimeError when sending job to the workers"""

    def __reduce__(self):
        raise RuntimeError()


if __name__ == "__main__":
    e = ProcessPoolExecutor()
    f = e.submit(id, ObjectWithPickleError())
    e.shutdown(wait=False)
    # f.result()  # Deadlock on get
