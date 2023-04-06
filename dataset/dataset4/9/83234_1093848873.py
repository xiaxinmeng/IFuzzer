class Some_Class:

    def error(self):
        if not getattr(self, 'boo', None):
            raise Exception(f'`class {self.__class__.__name__}:` raised some error!')


something = Some_Class()
something.error()