from unicodedata import normalize
def normalize_keys(data):
    return {
        normalize('NFKC', key): value
        for key, value in data.items()
    }

def test(μ):
    print(μ)