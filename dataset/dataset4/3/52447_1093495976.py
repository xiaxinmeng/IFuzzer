if not logMultiprocessing:
    self.processName = None
else:
    # Errors may occur if multiprocessing has not finished loading
    # yet - e.g. if a custom import hook causes third-party code
    # to run when multiprocessing calls import. See issue 8200
    # for an example
    try:
        self.processName = sys.modules['multiprocessing'].current_process().name
    except StandardError:
        self.processName = 'MainProcess'