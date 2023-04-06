import random

numbers = range(1, 50)
chosen = []

while len(chosen) < 6:
    number = random.choice(numbers)
    numbers.remove(number)
    chosen.append(number)

chosen.sort()
print("This week's numbers are", chosen)
print("The bonus ball is", random.choice(numbers))