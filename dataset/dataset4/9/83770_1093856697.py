
queue_listener = QueueListener(queue, handler)
queue_listener.start()
# queue messages
queue_listener.stop()
