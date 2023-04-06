@unittest.skipUnless(hasattr(logging.handlers, 'QueueListener'),
                     'logging.handlers.QueueListener required for this test')
def test_queue_listener_with_multiple_handlers(self):
    # Test that queue handler format doesn't affect other handler formats ([bpo-35726](https://bugs.python.org/issue35726)).
    self.que_hdlr.setFormatter(self.root_formatter)
    self.que_logger.addHandler(self.root_hdlr)

    listener = logging.handlers.QueueListener(self.queue, self.que_hdlr)
    listener.start()
    self.que_logger.error("error")
    listener.stop()
    self.assertEqual(self.stream.getvalue().strip(), "que -> ERROR: error")