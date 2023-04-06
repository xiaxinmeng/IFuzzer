import os
import sys
from multiprocessing import Process


class MyProcess(Process):

    def _bootstrap(self, parent_sentinel=None):
        """
        override to avoid deadlocks on termination
        it seems there is a race condition in flush()
        see: https://github.com/python/cpython/issues/91776
        """

        try:
            sys.stdout = os.fdopen(1, 'w')
        except Exception as ex:
            sys.stdout = None

        try:
            sys.stdout = os.fdopen(2, 'w')
        except Exception as ex:
            sys.stderr = None

        return super()._bootstrap(parent_sentinel=parent_sentinel)