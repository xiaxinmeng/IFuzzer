import gettext, pprint
with open("messages.mo", "rb") as fp:
    t = gettext.GNUTranslations()
    t._parse(fp)
    pprint.pprint(t._info)