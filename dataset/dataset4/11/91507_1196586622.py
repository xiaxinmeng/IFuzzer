@dataclass
class Reader(MixinClass, BaseClass):
    def show(self):
        print(f"repository: {self.repository}")
        print(f"filename: {self.filename}")
        print(f"path: {self.path}")