# Option 2 - RotatingFileHandler fails when created through yaml
handler = yaml.load("""
!!python/object/new:logging.handlers.RotatingFileHandler
    kwds:
        filename: test.log
        maxBytes: 262144
        backupCount: 3
""")