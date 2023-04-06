
with open('Files/config copy.yaml', 'r') as f:
        config_dict = yaml.safe_load(f.read())
        logging.config.dictConfig(config_dict)

logger = logging.getLogger("process_logger")
logger.debug('This is a debug message')
