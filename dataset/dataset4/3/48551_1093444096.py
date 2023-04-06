import multiprocessing, logging

def f():
    logger = multiprocessing.get_logger()
    logger.info('info from subprocess')

if __name__ == '__main__':
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    logger.info('info from main process')
    p = multiprocessing.Process(target=f)
    p.start()
    p.join()