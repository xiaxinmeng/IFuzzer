

class ModuleTemplate(ABC):

    @abstractmethod
    def _internal_main_operation(self, a: int, b: str, c: list) -> bool:
        pass

    @functools.wraps(_internal_main_operation)
    def external_main_operation(self, *args, **kwargs):
        print('LOG: Operation started.')
        try:
            ret = self._internal_main_operation(*args, **kwargs)
        except:
            print('LOG: Operation finished successfully.')
            raise
        else:
            print('LOG: Operation finished successfully.')

        return ret


class ModulePositiveCheck(ModuleTemplate):
    def _internal_main_operation(self, a: int, b: str, c: list) -> bool:
        return a > 0

