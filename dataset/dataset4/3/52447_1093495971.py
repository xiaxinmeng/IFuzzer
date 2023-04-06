if logMultiprocessing:
    try:
        self.processName = sys.modules['multiprocessing'] .current_process().name
    except StandardError:
        self.processName = 'MainProcess'
else:
    self.processName = None