# log gather state
logger.info(future_gather.cancelled())  # False / UNEXPECTED / ASSUMED BUG
logger.info(future_gather.done())  # True
logger.info(future_gather.exception())  # CancelledError
logger.info(future_gather._state)  # FINISHED

# log child state
logger.info(task_child.cancelled())  # True
logger.info(task_child.done())  # True
# logger.info(task_child.exception())  Raises because _state is CANCELLED
logger.info(task_child._state)  # CANCELLED