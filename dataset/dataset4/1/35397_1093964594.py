import select
poller = select.poll()
while 1:
  poller.register(101, 1)