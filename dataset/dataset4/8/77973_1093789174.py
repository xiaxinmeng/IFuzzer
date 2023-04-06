policy = asyncio.get_event_loop_policy()
policy._loop_factory = asyncio.ProactorEventLoop