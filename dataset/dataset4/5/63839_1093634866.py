import email
import http.client
import pickle
import test.regrtest
import test.test_os
import tracemalloc
import xmlrpc.server

snap = tracemalloc.take_snapshot()
with open("dump.pickle", "wb") as fp:
    pickle.dump(snap, fp, 2)