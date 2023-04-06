# 3rd solution
logging.config.dictConfig({
    "version": 1,
    "handlers": {
        "null": {
            "class": "logging.NullHandler"
        }
    },
    "loggers": {
        "foo": {
            "handlers": ["null"],
            "propagate": False
        }
    }
})