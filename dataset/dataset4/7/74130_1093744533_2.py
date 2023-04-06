class Stuff:  # Top of diamond, just so super().stuff() valid in all children
    def stuff(self):
        print("Stuff")

class Spam:
    def stuff(self):
        print("Spam")
        super().stuff()

class Eggs:
    def stuff(self):
        print("Eggs")
        super().stuff()

class SpamAndEggsWithoutSpam(Spam, Eggs):
    stuff = Eggs.stuff  # I'd like my stuff without Spam