def noErrorLogs(param):
    return 1 if param.levelno < 40 else 0

logconfig_dict = {
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["console"]},
    "version": 1,
}

logging.basicConfig()
dictConfig(logconfig_dict)
l = logging.getLogger()
l.handlers[0].addFilter(noErrorLogs)