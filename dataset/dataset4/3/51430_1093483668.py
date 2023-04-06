config.fileConfig('logging.cristiroma.config')
log = logging.getLogger('butterfly.test')
log.info('info')
log.error('error')