class AuthenticationString(bytes):
    def __reduce__(self):
        from .forking import Popen
        if not Popen.thread_is_spawning():
            raise TypeError(
                'Pickling an AuthenticationString object is '
                'disallowed for security reasons'
                )
        return AuthenticationString, (bytes(self),)