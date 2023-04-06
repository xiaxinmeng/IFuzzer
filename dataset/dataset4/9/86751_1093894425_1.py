def get_executor(self, args: tuple = (), kwargs: dict = {}):
    return get_context("spawn").Process(target=self._executor_target, args=args, kwargs=kwargs, daemon=True)