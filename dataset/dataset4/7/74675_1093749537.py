if key in throttle_dns_events:
    yield from throttle_dns_events[key].wait()
else:
    throttle_dns_events[key] = Event(loop=loop)
    try:
        addrs = yield from \
            resolver.resolve(host, port, family=family)
        cached_hosts.add(key, addrs)
        throttle_dns_events[key].set()
    except Exception as e:
        # any DNS exception, independently of the implementation
        # is set for the waiters to raise the same exception.
        throttle_dns_events[key].set(exc=e)
        raise
    finally:
        throttle_dns_events.pop(key)