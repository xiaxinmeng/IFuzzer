set_wakeup_fd(wakeup_fd)
block_for_io([wakeup_fd, ...])
try:
    explicitly_run_signal_handlers_even_though_they_are_deferred()
except KeyboardInterrupt:
    # arrange to deliver KeyboardInterrupt to some victim task
    ...