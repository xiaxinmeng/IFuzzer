
import logging

parent_handler = logging.StreamHandler()
child_handler = logging.StreamHandler()

parent_logger = logging.getLogger('parent')
child_logger = logging.getLogger('parent.child')

parent_logger.addHandler(parent_handler)
child_logger.addHandler(child_handler)

child_logger.disabled = True

child_logger.error("wops")
