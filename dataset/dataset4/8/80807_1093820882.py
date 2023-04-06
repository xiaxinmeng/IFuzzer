def cb_signal_handler(signum, frame):
    asyncio.get_event_loop().stop()


def main():
    signal.signal(signal.SIGINT, cb_signal_handler)