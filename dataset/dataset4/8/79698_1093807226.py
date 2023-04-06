if exclusive and hasattr(select, "EPOLLEXCLUSIVE"):
                    epoll_events |= select.EPOLLEXCLUSIVE