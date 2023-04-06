import re
cons_taml = "[கஙசஞடணதநபமயரலவழளறன]"
print(re.findall("\\b" + cons_taml + "ை|ஐ", "ஐவர் பையன் இசை சிவிகை இல்லை இவ்ஐ"))
cons_deva = "[कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह]"
print(re.findall("\\b" + cons_deva + "ै|ऐ", "ऐषमः तैलम् ईडै समीशै ईक्षै ईक्ऐ"))