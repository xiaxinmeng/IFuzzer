class WindowsProactorEventLoopPolicy(events.BaseDefaultEventLoopPolicy):
    _loop_factory = ProactorEventLoop