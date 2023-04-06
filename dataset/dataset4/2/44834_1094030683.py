def parse_dtd(dtd):
    parser = DTDParser()
    handler = DTDConsumerPE()
    parser.set_dtd_consumer(handler)
    parser.feed(dtd)

tracer.trace(DTDConsumer)