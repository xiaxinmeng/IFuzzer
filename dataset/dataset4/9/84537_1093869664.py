event_loop.create_task(event_loop.shutdown_default_executor())
event_loop.stop()
event_loop.run_forever()