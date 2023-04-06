import dataclasses
@dataclasses.dataclass
class FileObject:
    _uploaded_by: str = dataclasses.field(default=None, init=False)

    def _uploaded_by_getter(self):
        return self._uploaded_by

    def _uploaded_by_setter(self, uploaded_by):
        print('Setter Called with Value ', uploaded_by)
        self._uploaded_by = uploaded_by