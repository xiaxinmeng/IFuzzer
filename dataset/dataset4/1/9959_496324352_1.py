
class DefaultContext(BaseContext):
    @property
    def Process(self):
        class _Process(Process):
             _ctx = self.get_context()
        return _Process
