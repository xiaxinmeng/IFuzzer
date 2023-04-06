
a = "some_underscored_value"


u = (f" hello `{a}` cruel world"
     " hi")

print(u)

query = (f"SELECT COUNT(*) "
         "FROM `{a}` entry "
         "WHERE entry.type == 'device' "
         "AND entry.instance == {a}")

print(query)
