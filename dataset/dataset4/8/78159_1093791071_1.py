config = {
    "version": 1,
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "test.log"
        }
    },
    "root": {
        "handlers": ["file"]
    }
}
logging.config.dictConfig(config)
logging.config.dictConfig(config)
EOF