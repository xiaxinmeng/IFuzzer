if __name__ == '__main__':
    init('testing')
    logging.error("ohai")
    logging.debug("ohai debug")
    logging.getLogger().handlers[0].doRollover()
    logging.error("ohai next day")
    logging.debug("ohai debug next day")