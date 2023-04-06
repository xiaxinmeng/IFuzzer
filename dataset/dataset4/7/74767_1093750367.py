import logging
log_c = logging.getLogger('a.b.c')
log_a = logging.getLogger('a')
log_c.error("spam") # Doesn't showa