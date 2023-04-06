def mysighandler():
    pass

def do_loop(loop):
    loop.close()

loop = asyncio.new_event_loop()
loop.add_signal_handler(signal.SIGINT, mysighandler)
t = threading.Thread(target=do_loop, args=(loop,))
t.start()
t.join()