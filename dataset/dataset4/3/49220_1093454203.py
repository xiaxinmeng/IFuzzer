import os
try:
    # 'linuxthreads-0.10' or 'NPTL 2.10.2'
    pthread = os.confstr("CS_GNU_LIBPTHREAD_VERSION")
    linuxthreads = pthread.startswith("linuxthreads")
except ValueError:
    linuxthreads = False