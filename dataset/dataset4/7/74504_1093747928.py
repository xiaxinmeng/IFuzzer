class TCPServer:
    def close_request(self, request):
        try:
            request.close()
        except ConnectionError:
            # Suppress asynchronous errors such as ECONNRESET on Free BSD
            pass