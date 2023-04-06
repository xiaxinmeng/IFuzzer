import os
import pathlib
import sys

pl_path = pathlib.Path(__file__).parents[1].resolve()
sys.path.append(str(pl_path))



from src.Core.Logging import get_logger
#
logger = get_logger(__name__, False)
logger.info("TESTING_USing taskScheduler")