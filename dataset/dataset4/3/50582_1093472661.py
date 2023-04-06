import logging
import StringIO
stream = StringIO.StringIO()
logging.basicConfig(stream=stream)
stream.close() # to free memory/release resources