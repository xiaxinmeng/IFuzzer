# This works for FileHandler's
log = logging.getLogger('MyLog')
fh = logging.FileHandler('/some/file')

with daemon.DaemonContext(files_preserve=[fh.stream, ]):
   log.warn("In the belly of the beast.")