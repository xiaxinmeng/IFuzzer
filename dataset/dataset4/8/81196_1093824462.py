if spec is None and _is_async_obj(original):
    Klass = AsyncMock
else:
    Klass = MagicMock