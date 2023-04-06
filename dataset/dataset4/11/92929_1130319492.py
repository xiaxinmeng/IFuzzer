
with open(config_file_path.absolute(), 'r') as f:
    config_dict = yaml.safe_load(f.read())
    logging.config.dictConfig(config_dict)
