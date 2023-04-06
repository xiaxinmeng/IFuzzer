lower_map = string.maketrans(string.ascii_upper,
string.ascii_lower)
def _ascii_lower(str):
   return str.translate(lower_map)