class Spam:
    bar: typing.Optional[bar] = str

class Spaz:
    bar: typing.Optional[bar] = None

print(Spam.__annotations__)
print(Spaz.__annotations__)