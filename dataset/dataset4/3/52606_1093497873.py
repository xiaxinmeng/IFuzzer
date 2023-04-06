import gettext

gettext.bindtextdomain("pygettext_test","./locale")
gettext.textdomain("pygettext_test")
_=gettext.gettext
n_=gettext.ngettext

n1=1
n2=3