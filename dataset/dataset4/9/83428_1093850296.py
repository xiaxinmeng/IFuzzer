import dataclasses
import typing
@dataclasses.dataclass
class FileObject:
    uploaded_by:typing.Optional[None]=None

    def _uploaded_by_getter(self):
        return self._uploaded_by

    def _uploaded_by_setter(self, uploaded_by):
        print('Setter Called with Value ', uploaded_by)
        self._uploaded_by = uploaded_by

FileObject.uploaded_by = property(
    FileObject._uploaded_by_getter,
    FileObject._uploaded_by_setter
)
p = FileObject()
print(p)
print(p.uploaded_by)