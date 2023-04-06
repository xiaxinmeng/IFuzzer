class QueueHandlerTest(BaseTest):

    def test_formatting_exc_text(self):
        formatter = logging.Formatter(self.log_format)
        self.que_hdlr.setFormatter(formatter)
        try:
            raise RuntimeError('deliberate mistake')
        except:
            self.que_logger.exception('failed', stack_info=True)
        log_record = self.queue.get_nowait()
        self.assertTrue(log_record.exc_text.startswith('Traceback (most recent '
                                                       'call last):\n'))