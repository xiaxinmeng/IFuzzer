t = self.b.create_text(
    (point.baseX + 1)*self.checkerSize/2 + fudge,
    y + fudge,
    text = str(point.occupied),
    width = self.checkerSize)