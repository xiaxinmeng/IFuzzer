arcname = "hi"
arcname = arcname.translate(table)
# ascii strings are fine

arcname = u"hi"
arcname = arcname.translate(table)
# unicode fails
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: character mapping must return integer, None or unicode