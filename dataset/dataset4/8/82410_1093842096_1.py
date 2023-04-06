
import multiprocessing
import aiohttp


connection_key = aiohttp.client_reqrep.ConnectionKey
ose = OSError('test')

e = aiohttp.client_exceptions.ClientConnectorError(connection_key, ose)
q = multiprocessing.Queue()

q.put(e)
q.get(e)
