log_config = json.loads(log_config_txt)
logging.config.dictConfig(log_config)
logger = logging.getLogger("calculator")