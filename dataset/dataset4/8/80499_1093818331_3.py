import logging.config

# 1st solution
logging.config.dictConfig({
    "version": 1,
    "loggers": {
        "foo": {
            "disabled": True
        }
    }
})