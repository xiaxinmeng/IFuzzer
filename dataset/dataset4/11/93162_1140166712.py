listener_instance = MyQueueListener()

def configure_queue_instance(handlers_by_name):
    listener_instance.set_handler_by_names(handlers_by_name)
    return listener_instance

cfg = {
  'qhand': 'logging.handlers.QueueHandler',
  'queue': lambda: listener_instance.queue,
  'listener': 'my_module.configure_queue_instance'
}

setConfig(cfg)