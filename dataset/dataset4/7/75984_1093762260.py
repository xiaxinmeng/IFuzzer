if sys.platform == 'win32':
    time.clock = time.perf_counter
else:
    time.clock = time.process_time