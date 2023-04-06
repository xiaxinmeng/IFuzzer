import os
import unicodedata
upsilon_diaeresis_and_hook = "ϔ"

for form in ["NFC", "NFD", "NFKC", "NFKD"]:                       
  unicode_filename = unicodedata.normalize(form, upsilon_diaeresis_and_hook)
  with open(unicode_filename, "w") as f: f.write(form)
  print("N:", ascii(unicode_filename))
  print([ascii(filename) for filename in os.listdir('.')])