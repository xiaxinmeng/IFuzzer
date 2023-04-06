if create:
    from .resource_tracker import register
    register(self._name, "shared_memory")