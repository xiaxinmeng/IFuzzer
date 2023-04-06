def __iand__(self, c):
    for item in self - c:
        self.discard(item)