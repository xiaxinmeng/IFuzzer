from multiprocessing import Manager
manager = Manager()
ns_proxy = manager.Namespace()
evt_proxy = manager.Event()
ns_proxy.my_event_proxy = evt_proxy
print(ns_proxy.my_event_proxy)