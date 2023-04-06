import logging
import logging.config
import json
import pathlib
import os

config_location = pathlib.Path(  os.path.realpath(__file__) ).parent / "log.config"
log_config = json.load( config_location.open() )

logging.config.dictConfig(log_config)

logger = logging.getLogger("calculator")