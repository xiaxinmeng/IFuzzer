s = u"БГДЖИЛЦЫЭu042eЯАВЕКМРТu042312456789"
while True:
    state = random.getstate()
    try:
        a = random.choice(s)
    except IndexError:
        break