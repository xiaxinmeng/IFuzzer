query = ("SELECT COUNT(*) "
         f"FROM `{a}` entry "
         "WHERE entry.type == 'device' "
         f"AND entry.instance == {a}")