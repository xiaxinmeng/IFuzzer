import logging


config = {}
config['log'] = {}
config['log']['log_type'] = 'file'
config['log']['log_file'] = './log'
config['log']['config'] = { 'version' : 1 }


def do_config_logging():
    if config['log']['log_type'] == 'from_config':
        import logging.config
        logging.config.dictConfig(config['log']['config'])
    elif config['log']['log_type'] == 'file':
        logging.basicConfig(filename=config['log']['log_file'])
        logging.info("start logging")


if __name__ == "__main__":
    do_config_logging()