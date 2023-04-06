def encode(inputLetters):
    code = {'C':'D', 'F':'E'}
    return set(code[x] for x in inputLetters)