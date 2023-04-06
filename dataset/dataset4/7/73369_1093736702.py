class BaseHandler:
    ...
    def finish_response(self):
        try:
            ...
        except:
            # Limited version of “close” method on exception
            if hasattr(self.result, 'close'):
                self.result.close()
            raise
        self.close()  # Full “close” method when no exception