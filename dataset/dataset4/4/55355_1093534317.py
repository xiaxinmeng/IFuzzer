class Spam(object):
    def frobnicate(self):
        self.eggs = self.buy_eggs()
        self.scrambled = self.scramble(self.eggs)
        return self.scrambled > 42