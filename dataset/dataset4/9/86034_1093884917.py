class MySMTPClient(smtplib.SMTP):
    def __init__(self, *args, logger=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger
    def _print_debug(self, *args):
        if self.logger:
            self.logger.debug(" ".join(args))
        super()._print_debug(*args)