listener_instance = MyQueueListener()

cfg = {
  'qhand': 'logging.handlers.QueueHandler',
  'queue': lambda: listener_instance.queue,
  'listener': listener_instance.set_handler_by_names
}

setConfig(cfg)