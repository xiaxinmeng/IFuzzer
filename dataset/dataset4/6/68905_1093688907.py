import logging
import logging.handlers

from multiprocessing import Process
from time import sleep

fileHandler = logging.FileHandler( 'mylog.log' )
fileHandler.setLevel( 5 )

logger = logging.getLogger( None )

def process_logger():

    print( "process waiting" )
    sleep( 5 )
    print( 'process start' )

    logger = logging.getLogger( None )

    for num in range( 1, 10 ):
        logger.critical( "critical: %d" % num )
        sleep(1)

#
# if this is where the handler is added, the critical messages
# will go to the file
#
logger.addHandler( fileHandler )

processLogger = Process( target=process_logger )
processLogger.start()