
from unittest.mock import Mock
from multiprocessing.managers import SyncManager, listener_client

listener_client["faked"] = listener_client["xmlrpclib"] 
sm = SyncManager(serializer="faked")
