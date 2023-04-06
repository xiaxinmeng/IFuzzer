class PidfdChildWatcher(AbstractChildWatcher):

    def __init__(self):
        if not hasattr(os, "pidfd_open"):
             raise RuntimeError("os.pidfd_open() is unavailable.")
        ...