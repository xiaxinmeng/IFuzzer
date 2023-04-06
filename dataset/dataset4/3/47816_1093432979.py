if not line:
    # Presumably, the server closed the connection before
    # sending a valid response.
    if self._initial_response:
        raise BadStatusLine(line)
    else:
        raise ConnectionClosed("Stream ended before receiving response")