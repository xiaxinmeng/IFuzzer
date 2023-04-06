for subscriber in sorted(wkd, key=wkd.__getitem__):
    self.notify(subscriber, message)