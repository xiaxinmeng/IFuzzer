import logging
logger = logging.getLogger(name='main')
logger.setLevel(logging.INFO)
logger.error('XXX')
print("logger parent ", logger.parent) # Root is always the parent by default
print("logger parent handlers ", logger.parent.handlers) # No root handler since root is not configured which logging error does below
print("logger handler ", logger.handlers) # Empty and no parent (root) handler so calls lastResort
logging.error('ZZZ') # Sets the root handler
print("logger parent after logging ", logger.parent) # Root is parent
print("logger parent handlers after logging ", logger.parent.handlers) # Root handler is set
print("logger handler after logging ", logger.handlers) # Empty but has parent (root) handler so lastResort is not called
logger.error('XXX')