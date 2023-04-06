print('main process ID: {}'.format(os.getpid()))
with mp.Pool(4, initializer=initializer) as executor:
    executor.map(worker, range(20))