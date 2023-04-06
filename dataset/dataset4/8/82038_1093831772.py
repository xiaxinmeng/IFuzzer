import pyperf

class Logger(object):
    def __init__(self):
        self._levelprop = self.level = 0

    @property
    def levelprop(self):
        return self.level


logger = Logger()
ns = {'logger': logger}
runner = pyperf.Runner()
runner.timeit('read attribute', 'logger.level', globals=ns)
runner.timeit('read property', 'logger.levelprop', globals=ns)