import httplib


def testHTTPlib(host, url):
    http = httplib.HTTPConnection(host)
    try:
        http.request('GET', url)
        response = http.getresponse()
    except IOError:
        self._log.warning("Can't connect to %s", url)
        return False
    except socket.error:
        self._log.error("Socket error retrieving %s", url)
        return False
    except socket.timeout:
        self._log.warning("Timeout connecting to %s", url)
        return False
    else:
        try:
            data = response.read()
            return True
        except socket.timeout:
            self._log.warning("Timeout reading from %s", url)
            return False
    return False