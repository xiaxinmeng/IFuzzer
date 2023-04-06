class SocksSMTP(smtplib.SMTP):
    def _get_socket(self, host, port, timeout):
        return some_socket_like_object(...)