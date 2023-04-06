
# To lowercase
def kucukharfyap(s):
    return ud.normalize("NFC", s).replace('İ', 'i').replace('I', 'ı').lower()

# To uppercase
def buyukharfyap(s):
    return ud.normalize("NFC", s).replace('ı', 'I').replace('i', 'İ').upper()
