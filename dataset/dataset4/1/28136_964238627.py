
def text_len(text):
    return sum(
        0 if c == 'Q' else 1
        for c in text
    )
