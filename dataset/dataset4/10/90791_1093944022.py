MEMORY_SANITIZER = (
    '-fsanitize=memory' in _cflags or
    '--with-memory-sanitizer' in _config_args
)   