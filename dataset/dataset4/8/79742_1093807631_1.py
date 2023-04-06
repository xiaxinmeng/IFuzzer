import select
p = select.epoll()
p.register(1, select.EPOLLIN)
p.poll(0)