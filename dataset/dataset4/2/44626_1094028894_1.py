log_directory = get_option_from_config_file(...)
if not os.path.isabs(log_directory):
  # make log_directory absolute based on app directory.
  log_directory = os.path.join(app_directory, log_directory)