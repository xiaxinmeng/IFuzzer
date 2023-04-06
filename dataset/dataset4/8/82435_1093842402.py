
import aiohttp
import pickle


connection_key = aiohttp.client_reqrep.ConnectionKey
ose = OSError(1, 'unittest')
cce = aiohttp.client_exceptions.ClientConnectorError(connection_key, ose)
cce_pickled = pickle.dumps(cce)
pickle.loads(cce_pickled)
