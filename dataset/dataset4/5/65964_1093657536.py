from unicodedata import normalize, category
norm_char = normalize(char)[0]
is_id_first_char = norm_char_first == '_' or category(norm_char_first) in {"Lu", "Ll", "Lt", "Lm", "Lo", "Nl"}