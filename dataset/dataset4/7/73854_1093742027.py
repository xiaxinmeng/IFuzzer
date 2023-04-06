query = (f"SELECT COUNT(*) "
         f"FROM `{a}` entry "
         f"WHERE entry.type == 'device' "
         f"AND entry.instance == {a}")