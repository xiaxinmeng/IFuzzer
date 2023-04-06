def mocked_log(log_level):
    # Return a copy as the bot may modify the logger and we should always return the intial logger
    print('copying   %x' % id(logger))
    assert logger.handlers
    logger_new = copy.copy(logger)
    logger_new.setLevel(log_level)
    print('copied to %x' % id(logger_new))
    return logger_new