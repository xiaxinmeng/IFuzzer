@dataclass
class FileObject:
    _uploaded_by: str = field(init=False)

    @property
    def uploaded_by(self):
        return self._uploaded_by

    @uploaded_by.setter
    def uploaded_by(self, uploaded_by):
        print('Setter Called with Value ', uploaded_by)
        self._uploaded_by = uploaded_by