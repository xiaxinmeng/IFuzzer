class MultiError(ExceptionGroup):
    def __init__(self, failed_tasks):
        super.__init__(
            f"{len(tasks)} tasks failed",
            [t.exception for t in failed_tasks],
        )
        self.tasks = tasks
        # ... and set __note__ on each exception for nice tracebacks