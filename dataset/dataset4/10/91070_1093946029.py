import logging
from logging.handlers import SysLogHandler

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
basic_datefmt = '%m/%d/%Y %I:%M:%S %p'

syslog_format = logging.Formatter(fmt='SetupCDNGUI: %(message)s', datefmt=basic_datefmt)

sys_handler = SysLogHandler(address='/var/run/syslog')
#sys_handler.encodePriority(SysLogHandler.LOG_USER, SysLogHandler.LOG_ALERT)
# Tried with the above, but didn't make a difference.  Neither did not defining the address and letting it go to local host.
sys_handler.setFormatter(syslog_format)
root_logger.addHandler(sys_handler)


# None of these will show up.
logging.critical("CCC This is a test critical")
logging.error("EEE This is a test error")
logging.info("III Still a test")


# Comparatively this sends a message received just fine
import syslog

syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_USER)
syslog.syslog(syslog.LOG_NOTICE, 'QQQ test log')