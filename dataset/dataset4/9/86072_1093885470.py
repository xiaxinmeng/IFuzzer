

def noErrorLogs(param):
    return 1 if param.levelno < 40 else 0

logconfig_dict = {
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
            "filters": [noErrorLogs]
        }
    },
    "root": {"level": "DEBUG", "handlers": ["console"]},
    "version": 1,
}
dictConfig(logconfig_dict)
