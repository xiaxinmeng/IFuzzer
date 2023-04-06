
import logging
import warnings

root_logger = logging.getLogger()
root_logger.handle = print

def test(**kwargs):
    warnings.warn("warning-module", **kwargs)
    logging.warning("on-module", **kwargs)
    root_logger.warning("on-logger", **kwargs)

for stacklevel in range(5):
    print(f"{stacklevel=}")
    test(stacklevel=stacklevel)
