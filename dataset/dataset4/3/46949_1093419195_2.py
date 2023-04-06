from acooke.util.log import Log
log = Log(__name__)
[...]
class Foo(object):
    def my_method(self):
        log.debug("this works as expected")