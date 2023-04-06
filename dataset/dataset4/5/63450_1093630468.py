# XOR each byte of the roundKey with the state table
def addRoundKey(state, roundKey):
    for i in range(len(state)):
        state[i] = state[i] ^ roundKey[i]