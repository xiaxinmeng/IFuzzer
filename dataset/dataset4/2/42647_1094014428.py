import asynchat

class MyAsyncChat(asynchat.async_chat):
    error = 0
    def handle_error(self):
        self.error = 1
        asynchat.async_chat.handle_error(self)
    def push(self, data):
        self.error = 0
        asynchat.async_chat.push(self, data)
        return self.error