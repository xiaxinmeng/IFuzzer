def myUpper(inString):
    return inString.upper().replace('à', 'À').replace('ä', 'Ä').replace('è', 'È').replace('é', 'É').replace('ö', 'Ö').replace('ü', 'Ü')

def myLower(inString):
    return inString.lower().replace('À', 'à').replace('Ä', 'ä').replace('È', 'è').replace('É', 'é').replace('Ö', 'ö').replace('Ü', 'ü')

def myTitle(inString): # WARNING: converts all whitespace to a single space
    returnValue = []
    for theWord in inString.split():
        returnValue.append(myUpper(theWord[:1]) + myLower(theWord[1:]))
    return ' '.join(returnValue)