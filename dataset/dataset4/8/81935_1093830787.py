
if os.name == 'posix':
    import _multiprocessing
    import _posixshmem

    _CLEANUP_FUNCS.update({
        'semaphore': _multiprocessing.sem_unlink,
        'shared_memory': _posixshmem.shm_unlink,
    })
