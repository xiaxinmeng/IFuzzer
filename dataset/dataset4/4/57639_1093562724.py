@curry
def fold(function, start, sequence):
    if len(sequence) == 0:
        return start
    else:
        return fold(function, function(start, sequence[0]), sequence[1:])