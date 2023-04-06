
if sys.platform == "win32":
    new_event_loop = ProactorEventLoop
else:
    new_event_loop = SelectorEventLoop
